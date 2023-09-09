"""Importing module pandas for my function."""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris.csv")

def average(data):
    """"This is a mean function."""
    result = data.mean()
    return result

def med(data):
    """"This is a median function."""
    result = data.median()
    return result

def standard_deviation(data):
    """"This is a standard deviation function."""
    result = data.std()
    return result

print(average(df.iloc[:, 1]))
#print(med(df.iloc[:, 1]))
#print(standard_deviation(df.iloc[:, 1]))

def visualize_data(data, 
                   x_column, 
                   y_column, 
                   title=None, 
                   xlabel=None, 
                   ylabel=None):
    """
    Visualize data from a DataFrame using pandas' built-in plotting capabilities.

    Args:
        data (pd.DataFrame): The DataFrame containing the data.
        x_column (str): The column to be used for the x-axis.
        y_column (str): The column to be used for the y-axis.
        title (str, optional): Title for the plot. Defaults to None.
        xlabel (str, optional): Label for the x-axis. Defaults to None.
        ylabel (str, optional): Label for the y-axis. Defaults to None.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_column], data[y_column])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show(block = True)
