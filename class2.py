import numpy as np

randomNumpyArray = np.random.randint(1, 50, 10) # instead of 10, you can write a tuple with dimensions

print("\nprinting random array")
print(randomNumpyArray)

print("\nprinting dimensions")
print(randomNumpyArray.ndim)

print("\nreshaping")
print(randomNumpyArray.reshape((5,2)))

randomNumpyArray2 = np.random.randint(1, 50, (5,2))

print("\nrandom array with shape")
print(randomNumpyArray2)

shuffled = np.random.permutation(randomNumpyArray)

print("\nshuffling")
print(shuffled)

shuffled2 = np.random.permutation(randomNumpyArray2)

print("\nshuffling 2 dimensional array")
print(shuffled2) # when shuffling 2 dim array, it'll shuffle the rows, not the elements

sorting = np.sort(randomNumpyArray2)

print("\nordered numpy array 2")
print(sorting)


randomNumpyArray1 = np.random.randint(1, 20, 10)

print("\none dimensional array")
print(randomNumpyArray1)

print("\nslicing an array")
print(randomNumpyArray1[1:4:1])

print("\nslicing until index 7")
print(randomNumpyArray1[0:8:1])

print("\nalternating elements")
print(randomNumpyArray1[0::2])

print("\nreversing")
print(randomNumpyArray1[10:0:-1]) # can also be [::-1]

####### CLASS 3

# selecting a certain element
print("\nselecting one particular element")
print(randomNumpyArray1[0])

# selecting certain elements
print("\nselecting multiple elements")
print(randomNumpyArray1[[0, 2, 3, 5]]) # two sets of square brackets

# conditional slicing with even numbers
print("\nconditional slicing with even numbers")
print(randomNumpyArray1)
print(randomNumpyArray1[randomNumpyArray1%2 == 0])

print("\nselecting all numbers greater than 5")
print(randomNumpyArray1[randomNumpyArray1 > 5])

print("\ndoing operations with 2 lists")
randomNumpyArray3 = np.arange(1, 6) # x
randomNumpyArray4 = np.arange(10, 15) # y
print((2*randomNumpyArray3)+(randomNumpyArray4 - 3))

print("\ncalculating surface areas of different cylinders")
radii = np.random.randint(1, 10, 5)
heights = np.random.randint(1, 20, 5)

print(2 * radii * 3.14 * heights)