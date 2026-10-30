import numpy as np

marks = np.array([78,85,90,66,72,88,95,60])

np.sort(marks)

print(np.percentile(marks, 25))
print(np.percentile(marks, 50))
print(np.percentile(marks, 75))
avg = np.average(marks)
print(np.count_nonzero(marks > avg))
