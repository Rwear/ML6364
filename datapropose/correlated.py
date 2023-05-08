import pandas as pd
from sklearn.feature_selection import SelectKBest

# Load and merge datasets
data = pd.read_csv('../NY_sample.csv')

# Convert to datetime and extract features
data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])
data['pickup_hour'] = data['tpep_pickup_datetime'].dt.hour
data['pickup_day_of_week'] = data['tpep_pickup_datetime'].dt.dayofweek
data['pickup_month'] = data['tpep_pickup_datetime'].dt.month
data['dropoff_hour'] = data['tpep_dropoff_datetime'].dt.hour
data['dropoff_day_of_week'] = data['tpep_dropoff_datetime'].dt.dayofweek
data['dropoff_month'] = data['tpep_dropoff_datetime'].dt.month
# print(data['pickup_hour'])
data['day_type'] = data['dropoff_day_of_week'].apply(lambda x: 1 if x < 5 else 2)
data['hour_type'] = data['dropoff_hour'].apply(lambda x: 1 if 5 <= x < 12 else (2 if 12 <= x < 16 else (3 if 16 <= x < 22 else 4)))

data = data[data['payment_type'] == 1]
data['total_amount'] = data['total_amount'] - data['tip_amount']
data = data.drop(['fare_amount', 'tolls_amount'], axis=1)

# Correlation analysis
correlations = data.corr()['tip_amount'].sort_values(ascending=False)
print(correlations)

# Feature selection using SelectKBest
X = data.drop(columns=['tip_amount', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'])
y = data['tip_amount']
k_best = SelectKBest
print(k_best)