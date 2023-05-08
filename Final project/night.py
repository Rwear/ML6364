import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#%%
data = pd.read_csv('../output_sample.csv')

print(data.columns)

#%%
df = data[['tpep_pickup_datetime', 'passenger_count', 'trip_distance', 'fare_amount', 'payment_type', 'tip_amount']]
df = df[df['payment_type'] == 1]
df = df[['tpep_pickup_datetime', 'passenger_count', 'trip_distance', 'fare_amount','tip_amount']]
df.to_csv('cleaning_ny23.csv', index=False)
print(df.columns)
#%%
print(df)
#%%
# Convert to datetime and extract features
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
df['pickup_day_of_week'] = df['tpep_pickup_datetime'].dt.dayofweek
df['pickup_month'] = df['tpep_pickup_datetime'].dt.month
df['percent_tipped'] = df['tip_amount']/df['fare_amount']
#%%
print(df)
#%%
# Categorize pickup days as either weekdays or weekends
def categorize_day(day_of_week):
    if day_of_week < 5:
        return 'weekday'
    else:
        return 'weekend'


df['pickup_day_type'] = df['pickup_day_of_week'].apply(categorize_day)

# Create separate dataframes for weekdays and weekends
weekday_df = df[df['pickup_day_type'] == 'weekday']
weekend_df = df[df['pickup_day_type'] == 'weekend']

count_1 = df[df['passenger_count'] == 1]
count_2 = df[df['passenger_count'] == 2]
count_3 = df[df['passenger_count'] == 3]
count_4 = df[df['passenger_count'] == 4]
count_5 = df[df['passenger_count'] == 5]
count_6 = df[df['passenger_count'] == 6]

bins = np.arange(0, 1, 0.01)

pct_1 = np.histogram(count_1['percent_tipped'], bins=bins)[0] / len(count_1)
pct_2 = np.histogram(count_2['percent_tipped'], bins=bins)[0] / len(count_2)
pct_3 = np.histogram(count_3['percent_tipped'], bins=bins)[0] / len(count_3)
pct_4 = np.histogram(count_4['percent_tipped'], bins=bins)[0] / len(count_4)
pct_5 = np.histogram(count_5['percent_tipped'], bins=bins)[0] / len(count_5)
pct_6 = np.histogram(count_6['percent_tipped'], bins=bins)[0] / len(count_6)

#%%
# Calculate the proportion of people paying each tip percentage in the weekday dataframe


# Calculate the proportion of people paying each tip percentage in the weekend dataframe
# weekday_pct = np.histogram(weekday_df['percent_tipped'], bins=bins)[0] / len(weekday_df)
# weekend_pct = np.histogram(weekend_df['percent_tipped'], bins=bins)[0] / len(weekend_df)
#
# different_pct = (weekday_pct - weekend_pct)/weekday_pct

bin_labels = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]

fig, ax = plt.subplots()
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'black']

ax.plot(bin_labels, pct_1, label='1', color=colors[0])
ax.plot(bin_labels, pct_2, label='2', color=colors[1])
ax.plot(bin_labels, pct_3, label='3', color=colors[2])
ax.plot(bin_labels, pct_4, label='4', color=colors[3])
ax.plot(bin_labels, pct_5, label='5', color=colors[4])
ax.plot(bin_labels, pct_6, label='6', color=colors[5])

# ax.plot(bin_labels, weekday_pct, label='weekday', color=colors[1])
# ax.plot(bin_labels, weekend_pct, label='weekend', color=colors[2])

# ax.plot(bin_labels, different_pct, label='different', color=colors[0])

ax.set_xlabel('Percent Tipped')
ax.set_ylabel('Percentage of Passengers')
# ax.set_title('Percentage of Passengers by Percent Tipped and Pickup Day Range')
ax.set_title('Percentage of Passengers by Percent Tipped and passenger number')

plt.legend()
plt.figure(figsize=(240, 120))
plt.show()
#%%
weekday_pct = np.histogram(weekday_df['percent_tipped'], bins=bins)[0] / len(weekday_df) * 100
print(sum(np.histogram(weekday_df['percent_tipped'], bins=bins)[0]))
print(len(weekday_df))
# print(np.histogram(weekday_df['percent_tipped'], bins=bins)[0] / len(weekday_df) * 100)
#%%
print(len(weekday_df[weekday_df['tip_amount'] == 0])/len(weekday_df))