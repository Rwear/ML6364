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

# Visualize the tip amount for different pickup hour ranges and passenger counts
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16, 6))
sns.boxplot(x='pickup_hour_range', y='tip_amount', data=similar_distance_data, ax=ax1)
sns.boxplot(x='passenger_count', y='tip_amount', data=similar_distance_data, ax=ax2)

ax1.set_title('Tip Amount vs Pickup Hour Range')
ax2.set_title('Tip Amount vs Passenger Count')

plt.show()
