import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

print(f"Total sales: {np.sum(sales)}")
print(f"Average daily sales: {np.average(sales)}")
print(f"Highest Sales day: {np.argmax(sales)+1}")
print(f"Lowest Sales day: {np.argmin(sales)+1}")
print(f"Standard Deviation of sales: {np.std(sales)}")
avg = np.average(sales)
print(f"Total days where sales are above average: {np.count_nonzero(sales > avg)}")

