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

titanic_csv.info() #displaying complete information of the data frame, like data type of each rows, how many rows, how many columns

print("\nprinting the statistical summary using 'describe'")
print(titanic_csv.describe()) # only applied for the entire dataframe

print("\nprinting the shape of the csv")
print(titanic_csv.shape)

print("\nprinting three columns of the csv")
print(titanic_csv[["Name", "Fare", "Age"]])

print("\nprinting only one column of the csv")
print(titanic_csv[["Age"]]) # similar to a series !!

print("\nprinting the mean of only one column")
print(titanic_csv["Age"].mean()) # works bc one column is just a series, so you can apply series operations to it

print("\nprinting the maximum fare")
print(titanic_csv["Fare"].max())

print("\nprinting all the age values that are only greater than 60")
### METHOD 1
# ageGreaterThan50 = titanic_csv[titanic_csv["Age"] > 60] # sort of creates a separate dataframe in a manner
# print(ageGreaterThan50[["Name", "Age"]])

### METHOD 2
print(titanic_csv[titanic_csv["Age"] > 60][["Age", "Name"]]) # another method to do this

print("\nAll the people who's age 18 or greater, and travelling in Passenger class 1")
ageGreaterThan18Pclass1 = titanic_csv[(titanic_csv["Age"] > 18) & (titanic_csv["Pclass"] == 1)]
print(ageGreaterThan18Pclass1)