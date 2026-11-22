import numpy as np

# Create a NumPy array from 1 to 15
arr = np.arange(1, 16)

print("Original Array:", arr)

# 1. Values less than 8
less_than_8 = arr[arr < 8]
print("\nValues less than 8:", less_than_8)
print("Count:", len(less_than_8))

# 2. Values greater than or equal to 10
greater_equal_10 = arr[arr >= 10]
print("\nValues greater than or equal to 10:", greater_equal_10)
print("Count:", len(greater_equal_10))

# 3. All odd numbers
odd_numbers = arr[arr % 2 != 0]
print("\nOdd numbers:", odd_numbers)
print("Count:", len(odd_numbers))