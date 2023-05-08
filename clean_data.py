import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Load the dataset
# Replace 'path/to/your/dataset.csv' with the actual path to your dataset
data = pd.read_csv('NY_sample.csv')

# Convert tpep_pickup_datetime to pandas datetime format
data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])

# Add a new feature: day or night (1 if hour >= 18 or hour <= 6, else 0)
data['night'] = np.where(
    (data['tpep_pickup_datetime'].dt.hour >= 18) | (data['tpep_pickup_datetime'].dt.hour <= 6),
    1, 0)

# Select the features and target
features = data[['night', 'passenger_count', 'fare_amount', 'trip_distance']]
target = data['tip_amount']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predict and evaluate the model
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")
