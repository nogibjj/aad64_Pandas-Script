"""Importing module pandas for my function."""
import pandas as pd
df = pd.read_csv("iris.csv")

def avg(data):
    """"This is a mean function."""
    result = pd.mean(data)
    print(result)

avg(df.iloc[:, 1])
