import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression

# Load and merge datasets
# ny_df = pd.read_csv('../NY_sample.csv')
# chi_df = pd.read_csv('chicago_taxi_data.csv')
# data = pd.concat([ny_df, chi_df], ignore_index=True)
data = pd.read_csv('../NY_sample.csv')
data = data.drop(['store_and_fwd_flag', 'congestion_surcharge', 'payment_type'], axis=1)
# Convert to datetime and extract features
data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])
data['pickup_hour'] = data['tpep_pickup_datetime'].dt.hour
data['pickup_day_of_week'] = data['tpep_pickup_datetime'].dt.dayofweek
data['pickup_month'] = data['tpep_pickup_datetime'].dt.month
data['dropoff_hour'] = data['tpep_dropoff_datetime'].dt.hour
data['dropoff_day_of_week'] = data['tpep_dropoff_datetime'].dt.dayofweek
data['dropoff_month'] = data['tpep_dropoff_datetime'].dt.month

# Correlation analysis
# correlations = data.corr()['tip_amount'].sort_values(ascending=False)
# print(correlations)
#
# # Feature selection using SelectKBest
# X = data.drop(columns=['tip_amount', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'])
# y = data['tip_amount']
# k_best = SelectKBest(score_func=f_regression, k=10)
# k_best.fit(X, y)
# selected_features = X.columns[k_best.get_support()]
# print("Selected features using SelectKBest: ", selected_features)

# # Feature selection using RFE
# linear_regression = LinearRegression()
# rfe = RFE(estimator=linear_regression, n_features_to_select=10)
# rfe.fit(X, y)
# selected_features_rfe = X.columns[rfe.get_support()]
# print("Selected features using RFE: ", selected_features_rfe)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Filter the dataset for similar distance trips
similar_distance_data = data[(data['trip_distance'] >= 1) & (data['trip_distance'] <= 1.5)]

# Create a new column for pickup hour ranges
def map_hour_to_range(hour):
    if 5 <= hour < 12:
        return 'morning'
    elif 12 <= hour < 17:
        return 'afternoon'
    elif 17 <= hour < 21:
        return 'evening'
    else:
        return 'night'

similar_distance_data['pickup_hour_range'] = similar_distance_data['pickup_hour'].apply(map_hour_to_range)
similar_distance_data['percent_not_tipped'] = (similar_distance_data['total_amount'] - similar_distance_data['tip_amount']) / similar_distance_data['total_amount']

# Visualize the tip amount for different pickup hour ranges and passenger counts
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16, 6))
sns.boxplot(x='pickup_hour_range', y='percent_not_tipped', data=similar_distance_data, ax=ax1)
sns.boxplot(x='passenger_count', y='percent_not_tipped', data=similar_distance_data, ax=ax2)

ax1.set_title('Tip Amount vs Pickup Hour Range')
ax2.set_title('Tip Amount vs Passenger Count')

plt.show()