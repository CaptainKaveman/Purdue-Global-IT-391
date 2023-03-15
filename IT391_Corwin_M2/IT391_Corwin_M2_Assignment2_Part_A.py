#*********************************************************

#****Assignment 2, Part A, Section 1

#*********************************************************

print('********** Section 1 – Quick Sort **********\n')

# Integer array from the given code.
intArray = [6501, 9503, 7557, 5535, 5601, 9001, 9888, 8801, 9767, 7815]

# Function that will take an array that needs to be sorted into ascending order.
def sortAsc(sortedArray):
  # Checks if the array is empty.
  if sortedArray is None or len(sortedArray) == 0:
    print('Array is empty')
  else:
    return f'The array sorted is: {sorted(sortedArray)}' # Returns the sorted value of the array.

# Using an f-string to print the unsorted array.
print(f'The array unsorted is: {intArray}')

# Calling the function with the variable that I want to sort.
arr = sortAsc(intArray)
print(arr)


#*********************************************************

#****Assignment 2, Part A, Section 2

#*********************************************************

print('\n********** Section 2 – Bubble Sort **********\n')

# Creating the variable for the given array of integers.
bubbleArray = [5, 90, 35, 45, 150, 3]

# Function that will take a given array and sort it by comparing the number to the right of it. If the number is greater then they swap places.
def bubbleSort(array):
  # For loop to iterate through the array.
  for i in range(len(array) - 1):
    # Variable to check if a swap has occured.
    checkSwap = 0
    # For loop to  iterate through the array
    for j in range(0, len(array) - i - 1):
      # If statement to compare two adjacent numbers.
      if array[j] > array[j + 1]:
        # If the left number is greater then it will swap it
        array[j + 1], array[j] = array[j], array[j + 1]
        checkSwap = 1
        # If statement to break out of the for loop after all of the swaps have been made.
        if checkSwap == 0:
          break
  # Using an f-string to print the sorted array.
  print(f'The array sorted is: {array}')
# F-string print statement to print the unsorted array.
print(f'The array unsorted is: {bubbleArray}')
# Calling the function with the array variable as the parameter.
bubbleSort(bubbleArray)


#*********************************************************

#****Assignment 2, Part A, Section 3

#*********************************************************

print('\n********** Section 3 – Binary Search **********\n')

# Creating a function to search the array. The parameters are the array to seacrch and the targetted number.
def binarySearch(array, i):
  # Initiallizing the variables.
  answer = ''
  first = 0
  last = len(array) - 1
  middle = 0

  # Creating a while loop to check the array.
  while first <= last:
    middle = (first + last) // 2
    # Checking if the targetted number is present in the middle
    if array[middle] < i:
      first = middle + 1
    # Checking if the middle number is equal to i. If true it will print the location and break out of the loop.
    elif array[middle] == i:
      answer = f'{i} found at location {middle + 1}.'
      break
    else:
      last = middle - 1
  if first > last:
    answer = f'{i} is not present in the list.\n'
  print(answer)

# Calling the function to search the array for the targetted number.
binarySearch(sorted(intArray), 8801)
binarySearch(sorted(intArray), 7777)


# Input prompt to keep the window open.
input()