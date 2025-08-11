
import numpy as np
from scipy import stats

marks = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]
marks_array = np.array(marks)

mean = np.mean(marks_array)
median = np.median(marks_array)


mode_result = stats.mode(marks_array, keepdims=True)
mode = mode_result.mode[0]  # Extract mode value

std_dev = np.std(marks_array)

print(f"Marks: {marks}")
print(f"Mean: {mean:.2f}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Highest Mark: {np.max(marks_array)}")
print(f"Lowest Mark: {np.min(marks_array)}")

