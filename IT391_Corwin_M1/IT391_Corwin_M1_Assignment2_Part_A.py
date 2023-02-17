#*********************************************************

#****Assignment 2, Part A, Section 1

#*********************************************************

print('\n********** Section 1 **********\n')

# Function to obtain a word entered by the user.
def revString(word):
  # Variable to hold the word entered by the user that is reversed.
  reverseWord = ""
  # For statement to get each character in the word.
  for char in word:
    # Combining the characters in reverse and adding them to the variable.
    reverseWord = char + reverseWord
  return f'Your word in reverse is: {reverseWord}'

print(revString(input('Please enter a word to see it reversed: ')))

# Shorter method using the slice statement that is built in Python. [::-1] the -1 will start at the end of the string and step backwards.
# def revString(word):
#   return f'\nYour word in reverse is: {word[::-1]}'

# print(revString(input('Please enter a word: ')))

#*********************************************************

#****Assignment 2, Part A, Section 2

#*********************************************************

print('\n********** Section 2 **********\n')

# Creating an empty list for the shoppers queue.
shoppers = []
# Adding the name of the shoppers in the queue.
shoppers.append('Jane')
shoppers.append('Bob')
shoppers.append('Liza')
shoppers.append('Tom')
shoppers.append('Mary')

# Printing the number of shoppers in line using length function.
print(f'The number of shoppers at the grocery store is, {len(shoppers)}.')
# Printing the name of the first shopper inline which is the index of 0.
print(f'The first shopper in line is, {shoppers[0]}.')

# Adding two names to the shoppers queue.
shoppers.append('Stephen')
shoppers.append('Ellen')

# Removing three shoppers from the queue using the pop function and indexing the name at 0 to remove the first name from the list.
shoppers.pop(0)
shoppers.pop(0)
shoppers.pop(0)

# Printing the number of shoppers and the name of the first person in line.
print(f'The number of shoppers now in line is, {len(shoppers)}.')
print(f'The shopper currently first in line is, {shoppers[0]}.\n')

# Input request to keep the console window running until the user quits the program.
input('\nPress enter to close . . .')