import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("diamonds.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
