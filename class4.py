# dataframe is 2 dimensional label data structure where you have rows and columns, like a spreads sheet
# use version 3.12

import pandas as pd

# keys are strings

people = {"name":["prestin", "raeya", "ava"], "age":[14, 14, 14], "nationality": ["vietnamese-filipino", "indian", "korean-japanese-british"]}

print("printing the name, age, and nationality dataframe")

print(pd.DataFrame(people))

# every row is called a record
# csv = comma separated values
# reading a csv file into code
# r reads the code as raw data without consequences - in this case, the backslash

titanic_csv = pd.read_csv(r"C:\Users\Ravis\Documents\Riddhima\python\data science\titanic.csv")

print("\nshowing the titanic csv")

print(titanic_csv)

print("\nprinting the variable type of 'titanic_csv' variable")
print(type(titanic_csv))

print("\nprinting first 5 using 'head'")
print(titanic_csv.head())

print("\nprinting last 5 using 'tail'")
print(titanic_csv.tail())

titanic_csv.info()

print("\nprinting the statistical summary using 'describe'")
print(titanic_csv.describe())

print("\nprinting the shape of the csv")
print(titanic_csv.shape)

print("\nprinting only one column of the csv")
print(titanic_csv["Name"]) # similar to a series !!