from main import average, med, standard_deviation
import pandas as pd

dataset = {"Values": [1, 3, 5, 7, 9]}
testing_data = pd.DataFrame(dataset)
def testing_main_avg():
    assert average(testing_data['Values']) == 5

def testing_main_med():
    assert med(testing_data['Values']) == 5

def testing_main_std():
    assert standard_deviation(testing_data['Values']) == 3.1622776601683795
