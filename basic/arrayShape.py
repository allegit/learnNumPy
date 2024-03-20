import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

arr1 = np.array([1,2,3,4], ndmin=5)
print(arr1)
print('Shape of array: ', arr1.shape)

print("\n\nExample of Reshape from 1-D to 2-D...")

arrReShape = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr = arrReShape.reshape(4,3)
print(newArr)

print("\n\nExample of Reshape from 1-D to 3-D...")

arrReShape1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr1 = arrReShape1.reshape(2,3,2)
print(newArr1)