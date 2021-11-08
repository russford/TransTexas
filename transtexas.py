#!/usr/bin/env python3

from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
)

from datetime import date

#
# """
# Enable debug logging
# """
# import logging
# logging.basicConfig(level=logging.DEBUG)

class Activity (object):
    def __init__ (self, activity):
        self.id = activity["activityId"]
        self.start_date, self.start_time = activity["startTimeLocal"].split(" ")
        self.duration = activity["duration"]
        self.distance = activity["distance"]

    def __str__(self):
        return "{}\t{}\t{}\t{}\t{}".format(self.id, self.start_date, self.start_time, self.duration, self.distance)


today = date.today()


try:
    client = Garmin("joy628@hotmail.com", "Motomama43")
    client.login()
    activities = client.get_activities(0,1000)
    acts = [Activity(a) for a in activities]

    with open ("activities.txt", "w") as f:
        f.write("\n".join([str(a) for a in acts]))

except (
    GarminConnectConnectionError,
    GarminConnectAuthenticationError,
    GarminConnectTooManyRequestsError,
) as err:
    print("Error occurred during Garmin Connect Client init: %s" % err)
    quit()
except Exception:  # pylint: disable=broad-except
    print("Unknown error occurred during Garmin Connect Client init")
    quit()


#
# """
# Download an Activity
# """
# try:
#     for activity in activities:
#         activity_id = activity["activityId"]
#         print("client.download_activities(%s)", activity_id)
# except (
#     GarminConnectConnectionError,
#     GarminConnectAuthenticationError,
#     GarminConnectTooManyRequestsError,
# ) as err:
#     print("Error occurred during Garmin Connect Client get activity data: %s" % err)
#     quit()
# except Exception:  # pylint: disable=broad-except
#     print("Unknown error occurred during Garmin Connect Client get activity data")
#     quit()
#
#
# first_activity_id = activities[0].get("activityId")
# owner_display_name =  activities[0].get("ownerDisplayName")
#
# """
# Get activity details
# """
# print("client.get_activity_details(%s)", first_activity_id)
# print("----------------------------------------------------------------------------------------")
# try:
#     details = client.get_activity_details(first_activity_id)
#     splits = client.get_activity_split_summaries(first_activity_id)
#     splitd = client.get_activity_splits(first_activity_id)
#     print(details)
# except (
#     GarminConnectConnectionError,
#     GarminConnectAuthenticationError,
#     GarminConnectTooManyRequestsError,
# ) as err:
#     print("Error occurred during Garmin Connect Client get activity details: %s" % err)
#     quit()
# except Exception:  # pylint: disable=broad-except
#     print("Unknown error occurred during Garmin Connect Client get activity details")
#     quit()
#
