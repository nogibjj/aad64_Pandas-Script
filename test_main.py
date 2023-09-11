from main import average, med, standard_deviation, visualize_data
import pandas as pd

dataset = {"Values": [1, 3, 5, 7, 9]}
testing_data = pd.DataFrame(dataset)


def testing_main_avg():
    assert average(testing_data["Values"]) == 5


def testing_main_med():
    assert med(testing_data["Values"]) == 5


def testing_main_std():
    assert standard_deviation(testing_data["Values"]) == 3.1622776601683795


testing_main_avg()
testing_main_med()
testing_main_std()

# Testing Usage of Visualization function:
data = {"x": [1, 2, 3, 4, 5], "y": [2, 3, 5, 7, 11]}
testing_data2 = pd.DataFrame(data)

visualize_data(
    testing_data2, "x", "y", title="Line Plot Example", xlabel="X-axis", ylabel="Y-axis"
)
