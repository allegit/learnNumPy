import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print("Arr1: ", arr1)
print("Arr2: ", arr2)

arr = np.concatenate((arr1,arr2))
print("New Array 1-D: ", arr)

arr3 = np.array([[1,2], [3,4]])
arr4 = np.array([[5,6], [7,8]])

print("Arr3: ", arr3)
print("Arr4: ", arr4)

arr2D = np.concatenate((arr3,arr4), axis=0)
print("New Array 1-D: ", arr2D)

arr2D1 = np.concatenate((arr3,arr4), axis=1)
print("New Array 2-D: ", arr2D1)

arrStack1 = np.stack((arr1, arr2), axis=1)
print("New Array 2-D w/stack: ", arrStack1)

arrRowStack1 = np.hstack((arr1, arr2))
print("New Array 2-D w/row stack: ", arrRowStack1)

arrColumnStack1 = np.vstack((arr1, arr2))
print("New Array 2-D w/column stack: ", arrColumnStack1)

arrDepthStack1 = np.dstack((arr1, arr2))
print("New Array 2-D w/depth stack: ", arrDepthStack1)