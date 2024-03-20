import numpy as np

print("Iterating a 1-D array\n")
arr1D = np.array([1,2,3])
for x in arr1D:
    print(x)

print("\nIterating a 2-D array\n")
arr2D = np.array([[1,2,3], [4,5,6]])
for y in arr2D:
    print(y)

print("\nIterating the scalars in a 2-D array\n")
for x in arr2D:
    for y in x:
        print(y)

print("\nIterating a 3-D array\n")
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for y in arr3D:
    print(y)

print("\nIterating the scalars in a 3-D array\n")
for x in arr3D:
    for y in x:
        for z in y:
            print(z)

print("\nIterating a new 3-D array\n")
arr3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr3D):
    print(x)

print("\nIterating a new 2-D array in steps\n")
arr2D = np.array([[1,2,3,4], [5,6,7,8]])
for x in np.nditer(arr2D[:, ::2]):
    print(x)

print("\nIterating using a ndenumerate\n")
arr1D = np.array([1,2,3])
for idx, x in np.ndenumerate(arr1D):
    print(idx, x)