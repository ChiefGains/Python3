import numpy as np

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]

print('Mean:', np.mean(data))
print('Median:', np.median(data))
print('50th Percentile (median):', np.percentile(data, 50))
print('25th Percentile (median):', np.percentile(data, 25))
print('75th Percentile (median):', np.percentile(data, 75))
print('Standard Deviation:', np.std(data))
print('variance:', np.var(data))