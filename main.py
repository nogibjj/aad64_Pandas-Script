import pandas as pd
df = pd.read_csv("iris.csv")

def avg(data):
    result = pd.mean(data)
    print(result)

avg(df.iloc[:, 1])
