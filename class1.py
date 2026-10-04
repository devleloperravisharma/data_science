import numpy as np

print("starting list")

list = [1, 2, 3, 4, 5]
print(list)

for elements in range(len(list)):
    list[elements] += 1

print("new list")
print(list)

print(type(list))

numpyArray = np.array(list)

print(numpyArray)
print(type(numpyArray))

print(numpyArray+1) # quicker than doing a for loop

print((numpyArray + 10)-2)

numpyZeros = np.zeros(5)

print(numpyZeros)

intNumpyZeros = np.zeros(5, int) # the argument int makes them all integers

print(intNumpyZeros)

numpyOnes = np.ones(5)

print(numpyOnes)

stringNumpyOnes = np.ones(5, str) # the argument str makes them all strings

print(stringNumpyOnes)

numpyOnes23 = np.ones((2,3), int)

print(numpyOnes23)

print(numpyOnes23.ndim) # .ndim gives dimensions

# shape gives rows and columns

print(numpyOnes23.shape) # .shape gives the shape

numpyArray2 = np.arange(1, 10) # step = increment

print(numpyArray2)

print(numpyArray2.reshape((3,3))) # converted to a 3 x 3

shuffle = np.random.permutation(numpyArray2)

print(shuffle)

randomRange = np.random.randint(1, 50, 10)

print(randomRange)