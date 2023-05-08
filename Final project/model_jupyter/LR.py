import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
# Load the dataset
taxi_data = pd.read_csv("../NY_sample.csv")

taxi_data = taxi_data[(taxi_data['payment_type'] == 1) & (taxi_data['fare_amount'] > 0)
                      & (taxi_data['tip_amount'] > 0) & (taxi_data['trip_distance'] < 30)
                      & (taxi_data['tip_amount'] < 30)]
# Convert to datetime and extract features
taxi_data['tpep_pickup_datetime'] = pd.to_datetime(taxi_data['tpep_pickup_datetime'])
taxi_data['tpep_dropoff_datetime'] = pd.to_datetime(taxi_data['tpep_dropoff_datetime'])
taxi_data['pickup_hour'] = taxi_data['tpep_pickup_datetime'].dt.hour
taxi_data['pickup_day_of_week'] = taxi_data['tpep_pickup_datetime'].dt.dayofweek
taxi_data['pickup_month'] = taxi_data['tpep_pickup_datetime'].dt.month
taxi_data['dropoff_hour'] = taxi_data['tpep_dropoff_datetime'].dt.hour
taxi_data['dropoff_day_of_week'] = taxi_data['tpep_dropoff_datetime'].dt.dayofweek
taxi_data['dropoff_month'] = taxi_data['tpep_dropoff_datetime'].dt.month
# print(data['pickup_hour'])
taxi_data['day_type'] = taxi_data['dropoff_day_of_week'].apply(lambda x: 1 if x < 5 else 2)
taxi_data['hour_type'] = taxi_data['dropoff_hour'].apply(lambda x: 1 if 5 <= x < 12 else (2 if 12 <= x < 16 else (3 if 16 <= x < 22 else 4)))

# Select the columns for analysis
X = taxi_data[['trip_distance', 'hour_type', 'day_type', 'passenger_count']]
y = taxi_data['tip_amount']

# Create a linear regression object and fit the model
reg = LinearRegression()
reg.fit(X, y)

# coefficients = reg.coef_
print("Slope: ", reg.coef_[0])

# Make predictions using the model
y_pred = reg.predict(X)

# Visualize the relationship between fare_amount and tip_amount
# Visualize the relationship between trip_distance and tip_amount
plt.scatter(X['trip_distance'], y, alpha=0.5)
plt.plot(X['trip_distance'], y_pred, color='red')
plt.xlabel('Trip Distance')
plt.ylabel('Tip Amount')
plt.show()

# Calculate R-squared
r2 = r2_score(y, y_pred)
print("R-squared: ", r2)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y, y_pred)
print("MSE: ", mse)

