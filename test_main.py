from main import average, med, standard_deviation, visualize_data
import pandas as pd
import time
import resource

usage = resource.getrusage(resource.RUSAGE_SELF)
print(f"User CPU time: {usage.ru_utime} seconds")
print(f"System CPU time: {usage.ru_stime} seconds")
print(f"Maximum resident set size: {usage.ru_maxrss} bytes")
print(f"Page reclaims (soft page faults): {usage.ru_minflt}")
print(f"Page faults (hard page faults): {usage.ru_majflt}")
print(f"Swaps: {usage.ru_nswap}")
print(f"Block input operations: {usage.ru_inblock}")
print(f"Block output operations: {usage.ru_oublock}")
print(f"Voluntary context switches: {usage.ru_nvcsw}")
print(f"Involuntary context switches: {usage.ru_nivcsw}")

start_time = time.time()

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


end_time = time.time()
execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")
