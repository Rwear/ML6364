import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 1. 数据清洗和准备
data = pd.read_csv("../NY_sample.csv")
data = data.loc[:, ['tpep_pickup_datetime', 'passenger_count', 'fare_amount', 'tip_amount']]

data = data.dropna()
data["tpep_pickup_datetime"] = pd.to_datetime(data["tpep_pickup_datetime"])

# 2. 特征工程
data["pickup_month"] = data["tpep_pickup_datetime"].dt.month
data["pickup_hour"] = data["tpep_pickup_datetime"].dt.hour
data["pickup_weekday"] = data["tpep_pickup_datetime"].dt.weekday

data = pd.get_dummies(data, columns=["pickup_month", "pickup_hour", "pickup_weekday"])

# 3. 数据拆分
X = data.drop(columns=["tip_amount", "tpep_pickup_datetime"])
y = data["tip_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. 建立随机森林回归模型
model = RandomForestRegressor()  # Instantiate RandomForestRegressor

# 5. 模型训练
model.fit(X_train, y_train)

# 6. 模型预测
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

# 准备输入数据
input_data = pd.DataFrame({
    'passenger_count': [1],
    'fare_amount': [4],
    'tpep_pickup_datetime': ['05/07/2023 15:44']
})

# 对输入数据进行预处理
input_data["tpep_pickup_datetime"] = pd.to_datetime(input_data["tpep_pickup_datetime"])

input_data["pickup_month"] = input_data["tpep_pickup_datetime"].dt.month
input_data["pickup_hour"] = input_data["tpep_pickup_datetime"].dt.hour
input_data["pickup_weekday"] = input_data["tpep_pickup_datetime"].dt.weekday

input_data = pd.get_dummies(input_data, columns=["pickup_month", "pickup_hour", "pickup_weekday"])

# 检查输入数据的列是否与训练数据相同
missing_cols = set(X_train.columns) - set(input_data.columns)
for c in missing_cols:
    input_data[c] = 0
input_data = input_data[X_train.columns]

# 输出转化后的输入数据
print("转化后的输入数据：\n", input_data)

# 使用随机森林回归模型进行预测
predicted_tip_amount = model.predict(input_data)

# 输出预测结果
print("预测结果:", predicted_tip_amount)
