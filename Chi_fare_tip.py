import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
taxi_data = pd.read_csv("Chicago_sample.csv")

# Filter out rows where payment_type is equal to 2
taxi_data = taxi_data[(taxi_data['payment_type'] == "Credit Card") & (taxi_data['fare'] >= 0)]

# Select the columns for analysis
X = taxi_data[['fare']]
y = taxi_data['tips']

# Create a linear regression object and fit the model
reg = LinearRegression()
reg.fit(X, y)

# coefficients = reg.coef_

print("Slope: ", reg.coef_[0])

# Make predictions using the model
y_pred = reg.predict(X)

# Visualize the relationship between fare_amount and tip_amount
plt.scatter(X, y, alpha=0.5)
plt.plot(X, y_pred, color='red')
plt.xlabel('Fare Amount')
plt.ylabel('Tip Amount')
plt.show()
