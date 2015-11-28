import cPickle as pickle
from collections import defaultdict

all_data_original = pickle.load(open("all_data_original.p", "rb"))

# 4/20/2014 - Sunday,  5/26/2014 - Monday,  7/4/2014 - Friday,  9/1/2014 - Monday

holiday_list = set(["4/20/2014", "5/26/2014", "7/4/2014", "9/1/2014"])
holidays = defaultdict(list)
for time, lists in all_data_original.items():
    for row in lists:
        if row[1] in holiday_list:
            crap = [row[0], row[2].split(":")[0], float(row[3]), float(row[4])]
            holidays[row[1]].append(crap)

days = defaultdict(list)
for date, lists in holidays.items():
    for row in lists:
        days[row[0]].append(row[1:])

pickle.dump(holidays, open("holiday_data_by_date.p", "wb"))
pickle.dump(days, open("holiday_data_by_dayofweek.p", "wb"))
