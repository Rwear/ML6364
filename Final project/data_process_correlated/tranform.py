import pandas as pd

# 读取 Parquet 文件
df = pd.read_parquet('../../NY_Taxi/yellow_tripdata_2023-02.parquet')

# 将 DataFrame 保存为 CSV 文件
df.to_csv('NY_sample.csv', index=False)
