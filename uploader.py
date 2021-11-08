import webbrowser
from urllib import parse


last_date = "2021-08-13"
base_url = "https://docs.google.com/forms/d/e/1FAIpQLSfdtEo8deGXPrQMG0HseajMF4XpoDBNHOpKVL8np-siabbL8Q/viewform?mc_cid=4af05be18d&mc_eid=7d1f4e52bd&"
activity_url = "https://connect.garmin.com/modern/activity/"

data_dict = { "id": "1668001993",
              "date_yr": "983222470_year",
              "date_mo": "983222470_month",
              "date_dd": "983222470_day",
              "dur_hr": "1183095074_hour",
              "dur_mm": "1183095074_minute",
              "dur_ss": "1183095074_second",
              "dist": "1038738856",
              "time_hr": "1426124445_hour",
              "time_mm": "1426124445_minute",
              }

entry_dict = { "43702383": "Joy Comeau",
               "572126515": "9322",
               "1564363182": "Run/Walk"
               }

def get_activity_url(activity):
    yr, mo, day = activity[1].split("-")
    s_h, s_m, s_s = activity[2].split(":")
    dur_h = int(float(activity[3])) // 3600
    dur_m = int(float(activity[3])) // 60 - dur_h * 60
    dur_s = int(float(activity[3])) - dur_h * 3600 - dur_m * 60
    dist = "{0:.2f}".format(int(float(activity[4])) / 1609)
    url_id = activity_url + activity[0]

    entry_dict[data_dict["id"]] = url_id
    entry_dict[data_dict["date_yr"]] = yr
    entry_dict[data_dict["date_mo"]] = mo
    entry_dict[data_dict["date_dd"]] = day
    entry_dict[data_dict["dur_hr"]] = dur_h
    entry_dict[data_dict["dur_mm"]] = dur_m
    entry_dict[data_dict["dur_ss"]] = dur_s
    entry_dict[data_dict["time_hr"]] = s_h
    entry_dict[data_dict["time_mm"]] = s_m
    entry_dict[data_dict["dist"]] = dist

    d = { "entry."+k: v for k, v in entry_dict.items() }

    return base_url+parse.urlencode(d)



with open ("activities.txt", "r") as f:
    data = [l.split('\t') for l in f.readlines()]

data = [d for d in data if d[1] > last_date]

with open("urls.txt", "w") as f:
    f.writelines([get_activity_url(a)+'\n' for a in data])