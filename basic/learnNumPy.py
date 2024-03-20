import numpy

arr0D = numpy.array(42)
print(str(arr0D.ndim) + "-dimensional array")
print("Value = " + str(arr0D) + "\n")

arr1D = numpy.array([1,2,3,4,5])
print("Type of array is " + str(type(arr1D)))
print(str(arr1D.ndim) + "-dimensional array")
print("Value = " + str(arr1D))
print("First Element = " + str(arr1D[0]))
print("Printing elements 1 to 5: " + str(arr1D[0:5]))
print("\n")

arr2D = numpy.array([[1,2,3], [4,5,6]])
print(str(arr2D.ndim) + "-dimensional array")
print("Value = " + str(arr2D) + "\n")

arr3D = numpy.array([[[1,2,3], [4,5,6]], [[7,8,9], [6,5,4]]])
print(str(arr3D.ndim) + "-dimensional array")
print("Value = " + str(arr3D) + "\n")

arrMul = numpy.array([1,2,3,4], ndmin=5)
print(str(arrMul.ndim) + "-dimensional array")
print("Value = " + str(arrMul) + "\n")