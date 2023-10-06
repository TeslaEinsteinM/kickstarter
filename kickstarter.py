import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

df = pd.read_csv('dataset.csv', encoding="ISO-8859-1")

# mean of pledged
mean = df['pledged'].mean()
print(mean)

# -----------------------------------------------------
# plot a histogram for backers and check the skewness
backers = df['backers']

bins = []
for i in range(200):
    if i % 10 == 0:
        bins.append(i)

plt.hist(backers, bins=bins, edgecolor='black')
plt.title('Distribution of Backers')
plt.xlabel('Number of Backers')
plt.ylabel('Frequency of Backers')
plt.show()
# -----------------------------------------------------
# plot the histogram for the duration of the projects
duration = df['duration']

plt.hist(duration, bins=bins, edgecolor='black')
plt.title('Duration of the Project')
plt.xlabel('Number of Days')
plt.ylabel('Frequency')
plt.show()
# -----------------------------------------------------
# number of successful projects
success_count = 0
# number of failed projects
fail_count = 0
# number of live projects
live_count = 0
# number of suspended projects
suspended_count = 0
# number of cancelled projects
cancelled_count = 0
# total number of days of all successful projects
success_duration = 0
# day the project kickstartet
funded_date = []
# -------------------------------------
# total number of projects
total = 0
# list of amounts successful projects received
amount = []
# dictionary of cateories of successful projects and their count
category_map = {}


# list of subcategory of the music that were the most successful
music_category = []
# all category
category = []

# loop through the data csv data gained from df to extract important informations
for index, row in df.iterrows():
    total += 1
    category.append(row['category'])
    # get the stats of successful projects
    if row['status'] == 'successful':
        key = row['category']
        category_map[key] = category_map.get(key, 0) + 1
        success_count += 1
        success_duration += row['duration']
        amount.append(row['goal'])
        funded_date.append(row['funded date'])
    # status of the projects
    if row['status'] == 'failed':
        fail_count += 1
    if row['status'] == 'canceled':
        cancelled_count += 1
    if row['status'] == 'live':
        live_count += 1
    if row['status'] == 'canceled':
        cancelled_count += 1
    if row['status'] == 'suspended':
        suspended_count += 1
    # get the status of the successful project's sub-category
    if row['status'] == 'successful' and row['category'] == 'Music':
        music_category.append(row['subcategory'])
# -------------------------------------------
# output the results
print(f'Success: {success_count}')
print(f'Fail: {fail_count}')
print(f'live: {live_count}')
print(f'Suspended: {suspended_count}')
print(f'Cancelled: {cancelled_count}')

print(f'Total: {total}')
# average amount get by successful projects
print(sum(amount)/len(amount))
# success ratio
print(f'Success ratio: {(success_count/total)*100}')
print(
    f'Average duration of successful Projects: {success_duration/success_count}')

# -------------------------------------------
ideal_project = ''
ideal_project_times = 0
for key, value in category_map.items():
    if value > ideal_project_times:
        ideal_project = key
        ideal_project_times = value
print(ideal_project, ideal_project_times)

print(Counter(music_category))
print(Counter(category))


day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = []
months = []

for date in funded_date:
    for d in day:
        if d in date:
            days.append(d)
print('#-----------------------')
for date in funded_date:
    for m in month:
        if m in date:
            months.append(m)

print(Counter(days))
print(Counter(months))
