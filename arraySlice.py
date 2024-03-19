import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print("Positive Slicing: " + str(arr[:6]))
print("Negative Slicing: " + str(arr[-7:-1]))
print("Step slicing:     " + str(arr[0:6:2]))