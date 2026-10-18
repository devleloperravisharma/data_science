import pandas as pd

random = [6, 2,88, 1, 23, 9, 16, 21, 21]

print(random)

series = pd.Series(random)

print(series) # left side is the index, right side are the elements, but you can change the left side since it's just a "label"

series2 = pd.Series(random, index = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"])

print("\nprinting a new set of labels using strings")

print(series2)

print("\nprinting the mean")

print(series2.mean())

print("\nprinting the sum")

print(series2.sum())

# mean, median, mode, sum, count, min, max are the basic statistical operators of pd

print("\nprinting the median")

print(series2.median())

print("\nprinting the mode")

print(series2.mode()) # modes will always be printed as a series because you can have multiple modes !!

print("\nprinting the count")

print(series2.count())

print("\nprinting the minimum value")

print(series2.min())

print("\n printing the maximum value")

print(series2.max())

print("\nsorting the series")

print(series2.sort_values())

print("\nsorting in descending order")

print(series2.sort_values(ascending=False))

print("\ncounting the number of times each value is written")

print(series2.value_counts())