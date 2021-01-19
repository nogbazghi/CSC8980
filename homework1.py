import pandas as pd
import numpy as np

# Write a function that finds the factorial of a number. Test the function finding the factorial of the number 10.
number = 10
def findFactorial(num):
  factorial = 1
  for digit in range(1, num):
    factorial = factorial * digit
  print("factorial: " + str(factorial))
  return factorial
findFactorial(number)

# Write a function that determines if a number is a prime number. Test the function with the following numbers: 3 and 1251.
numbers = [3, 1251]
def checkIfPrime(number):
  isItPrime = True
  for digit in range(2, number-1):
    if number%digit == 0:
      isItPrime = False
  return isItPrime

for number in numbers:
  value = checkIfPrime(number)
  print(str(number) + " is prime? " + str(value))

# Write a function that transposes a matrix. Test with a 3 x 3 identity matrix.
matrix = [[7, 7, 0], [6, 7, 8], [4, 0, 4]]
def transposeMatrix(matrix):
  transposed_matrix = []
  for row in matrix:
    for index in range(0, len(row)):
      digit = row[index]
      if len(transposed_matrix) < len(row):
        transposed_matrix.append([digit])
      else:
        updateList = transposed_matrix[index]
        updateList.append(digit)
        transposed_matrix[index] = updateList
  return transposed_matrix
print(transposeMatrix(matrix))

# Using Pandas and Numpy, write a piece of code to combine two series into one. Test your code with:
#
# np.random.seed(0)
# series1 = pd.Series(np.arange(10))
# series2 = pd.Series(np.arange(26))
# Do not forget to set the seed, or your answer won’t be reproducible.
series1 = pd.Series(np.arange(10))
series2 = pd.Series(np.arange(26))
def combineSeries(seed, one, two):
  np.random.seed(seed)
  newseries = one.combine_first(two)
  return newseries

print(combineSeries(0, series1, series2))

# Using pandas, write a piece of code to convert the first character of each element in a series to uppercase. Test your code with:
# 
# series = pd.Series(['nlp', 'will', 'be', 'easy?'])
series = pd.Series(['nlp', 'will', 'be', 'easy?'])
capitalized = series.str.capitalize()
print(capitalized)

# Bonus: Using pandas, write a piece of code to get the frequency of unique values in the entire dataframe (not using built in functions). Test your code with:
#
# dataFrame = pd.DataFrame(np.random.randint(5, 10, 20).reshape(-1, 4), columns = list('abcd'))
dataFrame = pd.DataFrame(np.random.randint(5, 10, 20).reshape(-1, 4), columns = list('abcd'))
def uniqueValueFrequency(df):
  cols = df.columns.values
  rows = df.index.values
  uniqueValue = dict()
  for col in cols:
    items = df[col]
    for row in rows:
      digit = items[row]
      if digit in uniqueValue.keys():
        updatedCount = uniqueValue[digit] + 1
        uniqueValue[digit] = updatedCount
      else:
        uniqueValue[digit] = 1
  return uniqueValue
print(uniqueValueFrequency(dataFrame))