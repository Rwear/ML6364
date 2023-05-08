import pandas as pd

# # read the csv file
# df = pd.read_csv('Chicago_sample.csv')
#
# print(df.columns)
#
# df = df.drop(['pickup_census_tract', 'dropoff_census_tract',
#        'pickup_community_area', 'dropoff_community_area'], axis=1)
# print(df.loc[df['taxi_id'] == 7418, 'trip_total'].iloc[0])
#
# df['trip_total'] = df['trip_total'] - df['extras']
#
# df = df.drop(['tolls', 'extras','company',
#        'pickup_latitude', 'pickup_longitude', 'dropoff_latitude',
#        'dropoff_longitude'], axis=1)
#
# print(df.loc[df['taxi_id'] == 7418, 'trip_total'].iloc[0])
# print(df)
# df.to_csv('clean_sample.csv', index=False)

nf = pd.read_csv('NY_sample.csv')

print(nf.columns)

nf.drop(['VendorID', 'tpep_pickup_datetime', 'RatecodeID', 'store_and_fwd_flag',
       'PULocationID', 'DOLocationID', 'payment_type', 'extra',
       'mta_tax', 'tolls_amount', 'improvement_surcharge', 'total_amount', 'congestion_surcharge'], axis=1, inplace=True)

nf.to_csv("NY_merge_sample")
print(nf.columns)
#
# nf = nf.drop(['VendorID','RatecodeID', 'store_and_fwd_flag','PULocationID', 'DOLocationID'], axis=1)
# print(df.loc[df['taxi_id'] == 7418, 'trip_total'].iloc[0])
#
# df['trip_total'] = df['trip_total'] - df['extras']
#
# df = df.drop(['tolls', 'extras','company',
#        'pickup_latitude', 'pickup_longitude', 'dropoff_latitude',
#        'dropoff_longitude'], axis=1)
#
# print(df.loc[df['taxi_id'] == 7418, 'trip_total'].iloc[0])
# print(df)
# df.to_csv('clean_sample.csv', index=False)