import numpy as np

randomNumpyArray = np.random.randint(1, 50, 10) # instead of 10, you can write a tuple with dimensions

print("printing random array")
print(randomNumpyArray)

print("printing dimensions")
print(randomNumpyArray.ndim)

print("reshaping")
print(randomNumpyArray.reshape((5,2)))

randomNumpyArray2 = np.random.randint(1, 50, (5,2))

print("random array with shape")
print(randomNumpyArray2)

shuffled = np.random.permutation(randomNumpyArray)

print("shuffling")
print(shuffled)

shuffled2 = np.random.permutation(randomNumpyArray2)

print("shuffling 2 dimensional array")
print(shuffled2) # when shuffling 2 dim array, it'll shuffle the rows, not the elements

sorting = np.sort(randomNumpyArray2)

print("ordered numpy array 2")
print(sorting)


randomNumpyArray1 = np.random.randint(1, 20, 10)

print("one dimensional array")
print(randomNumpyArray1)

print("slicing an array")
print(randomNumpyArray1[1:4:1])

print("slicing until index 7")
print(randomNumpyArray1[0:8:1])

print("alternating elements")
print(randomNumpyArray1[0::2])

print("reversing")
print(randomNumpyArray1[10:0:-1]) # can also be [::-1]