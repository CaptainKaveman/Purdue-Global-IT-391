#*********************************************************

#****Assignment 2, Part B, Section 1

#*********************************************************

print('\n********** Section 1 **********\n')

# Creating an empty list to hold the customers of the bank.
customers = []

# Adding the customers to the empty list.
customers.append('Jim')
customers.append('Bob')
customers.append('Susan')
customers.append('Liz')
customers.append('Alex')

# Printing the number of customers that are in line at the bank.
print(f'The number of people in the line at the bank is, {len(customers)}.')

print('\nThe names of those in line at the bank are,')
# Using a for loop to print the customers names that are in line at the bank.
for i in range(len(customers)):
  print(customers[i])
# Printing the first customer that is in line.
print(f'\nThe first customer in line is, {customers[0]}.')
customers.pop(0) # Removing the first cusomter from the list.

# Adding two new customers to the list.
customers.append('Andy')
customers.append('Rhonda')

# Removing the first three customers from the list.
customers.pop(0)
customers.pop(0)
customers.pop(0)
# Printing the number of customers in the line after the changes to the list.
print(f'The number of customers in line now is, {len(customers)}\n')

#*********************************************************

#****Assignment 2, Part B, Section 2

#*********************************************************

print('\n*********** Section: 2 ***********\n')

# Getting the input from the user for a sentence.
sentence = input('Please enter a sentence.\n')
# Taking the sentence and splitting it into a list of words using the Split function.
words = sentence.split()

# For loop to go through the list of words and remove them and print the results in reverse order.
for i in range(len(words)):
  print(words.pop())

# Input request to keep the console window running until the user quits the program.
input('\nPress enter to close . . .')