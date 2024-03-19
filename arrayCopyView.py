import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()
print("\n This is an example of copy\n\n")
print("Original array before modifying = " + str(x))
arr[0] = 42
print("Original array after modifying = " + str(arr))

print("\n\n This is an example of view\n\n")

y = x.view()
x[0] = 42
print("Original array after modifying = " + str(y))
print("Original array before modifying = " + str(x))

print("\n\n Make Changes in the VIEW: \n\n")

a = np.array([1,2,3,4,5])
b = a.view()
b[0] = 31
print("Original array after modifying = " + str(a))
print("Original array before modifying = " + str(b))
