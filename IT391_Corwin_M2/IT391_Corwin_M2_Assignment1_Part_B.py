#*********************************************************

#****Assignment 1, Part B, Section 1

#*********************************************************

# Creating an empty array to hold the list of mammals
mammals = []

# Using the append method to add each element to the list.
mammals.append('Bear')
mammals.append('Gorilla')
mammals.append('Tiger')
mammals.append('Polar Bear')
mammals.append('Lion')
mammals.append('Monkey')

# Creating a variable and turning the list into a set.
setMammals = set(mammals)

print('\n*********** Section: 1 ***********\n')

# Using an f-string to print the list or mammals from the set.
print(f'Contents of the set are:\n{setMammals}')

# Sorting the set with the built-in sort method.
sortedMammals = sorted(setMammals)

# F-string to print the sorted list of mammals.
print(f'\nContents of the sorted set are:\n{sortedMammals}')

# Printing the first item in the list which is at index 0.
print(f'\nThe first item in the set is: {sortedMammals[0]}')

# Printing the last item in the list. Using -1 will start at the end of the list.
print(f'\nThe last item in the set is: {sortedMammals[-1]}')

#*********************************************************

#****Assignment 1, Part B, Section 2

#*********************************************************

# Creating an empty variable to hold the dictionary of friends. Using dictionary allows the user to store the name of the person as a key and the phone number as a value. This will allow the user to easilty edit the phone number if it changes.
myFriends = {}

print(myFriends)

# Adding the [key] to the list followed by its value.
myFriends['Fred'] = '602-299-3300'
myFriends['Ann'] = '602-555-4949'
myFriends['Grace'] = '520-544-9898'
myFriends['Sam'] = '602-343-8723'
myFriends['Dorothy'] = '520-689-9745'
myFriends['Susan'] = '520-981-8745'
myFriends['Bill'] = '520-456-9823'
myFriends['Mary'] = '520-788-3457'

print('\n*********** Section: 2 ***********\n')

print('The contents of my friends list.\n')

# For loop to print each friend on a new line.
for key, value in myFriends.items():
  print(f'{key} {value}')

# Try/Catch block to remove elements from my friends list. If the key is in the dictionary it will remove it. If the key is not in the dictionary it will throw an exception.
try:
  myFriends.pop('Bill')
  myFriends.pop('Fred')
  myFriends.pop('Mary')
except KeyError:
  print('\nThat name is not in the list of friends.\n')

# Updating the phone number for Mary.
myFriends.update({'Mary':'520-897-4567'})

print('\nThe updated contents of my friends list.\n')

# For loop to print each friend on a new line.
for key, value in myFriends.items():
  print(f'{key} {value}')

# Using the len() function to give me the number of elements in the list.
print(f'\nThe number of friends in my list is: {len(myFriends)}\n')

# If statement to check if a key is in the list. If the name isn't in the list the else statement will print.
if 'Fred' in myFriends:
  print('Fred is still present in my list')
else:
  print('Fred is not present in my list')

#*********************************************************

#****Assignment 1, Part B, Section 3

#*********************************************************

print('\n*********** Section: 3 ***********')

# Ran out of time . .

#input()