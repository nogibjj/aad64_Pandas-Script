"""Importing module pandas for my function."""
import pandas as pd
df = pd.read_csv("iris.csv")

def avg_88(data):
    """"This is a mean function."""
    result = data.mean()
    return result

print(avg_88(df.iloc[:, 1]))
