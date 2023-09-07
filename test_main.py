from main import avg
import pandas as pd

dataset = {"Values": [1, 3, 5, 7, 9]}
df = pd.DataFrame(dataset)

def testing_main(data):
    test_result = avg(df)
    assert test_result == 5