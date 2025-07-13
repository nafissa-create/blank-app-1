import pandas as pd 
#load the data
df = pd.read_csv("diamonds.csv")
#print(df.head())
#see the number of rows and columns
print(df.shape)
#define the variables x and y for the linear regression model
x = df[["carat","clarity","table"]]
y = df["price"]
#convert categoriel variables into numeric
x = pd.get_dummies(x, columns = ["clarity"], drop_first = True)
print(x.columns)
print(df['clarity'].unique())

#split the data, data for training and data for testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape)
print(x_test.shape)

#create the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

#model performence
from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"the mean suared error is {mse}")
print(f"the r squared score is {r2}")

#save the model
import joblib
joblib.dump(model, "linear_model.pkl")
joblib.dump(x.columns.tolist(), "model_columns.pkl")


