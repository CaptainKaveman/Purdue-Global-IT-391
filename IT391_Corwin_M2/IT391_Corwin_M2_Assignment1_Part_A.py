#*********************************************************

#****Assignment 1, Part A, Section 1

#*********************************************************

# Profession array from the provided code example
profession_array = ['Software Engineer', 'Programmer', 'Database Admin', 'Network Admin', 'Web Developer', 'Program Manager']

# Creating a set using the array of professions
profession_set = set(profession_array)

# Sorting the set using the built in method sorted.
sorted_set = sorted(profession_set)

print('\n*********** Section: 1 ***********')

# Printing the orginal list of professions. Using an f sting I print the title of Orginal list on a new line and then print the list below it.
print(f'\nOriginal List:\n{profession_set}')
#print(profession_set) # Optional way to print the list on a new line. I prefer using f-stings when possible.

# Printing the sorted list of professions. Using an f sting I print the title of Sorted list on a new line and then print the list below it.
print(f'\nSorted List:\n{sorted_set}')
#print(sorted_set) # Optional way to print the list on a new line. I prefer using f-stings when possible.


#*********************************************************

#****Assignment 1, Part A, Section 2

#*********************************************************

print('\n*********** Section: 2 ***********')

# Creating the empty list for book titles.
books = []


# Adding the title of the book to the list. Using the append method will add the title to the end of the list.
books.append('To Kill a Mockingbird')
books.append('Huckleberry Finn')
books.append('Pride and Prejudice')
books.append('Brave New World')
books.append('Lord of the Flies')
books.append('Alice in Wonderland')
books.append('The Old Man and the Sea')
books.append('Atlas Shrugged')

# Printing the original list of books using an f-string.
print(f'\nOriginal Book List:\n{books}')

# Sorting the list of books using the built-in sorted method and saving the list to a new variable.
sorted_books = sorted(books)

# Printing the sorted list of books using an f-string.
print(f'\nSorted Book List:\n{sorted_books}')

# Removing items for the sorted list using the pop method.
sorted_books.pop(1) # This will remove the second book from the list which is at index 1. The first item is at index 0.
sorted_books.pop(0) # This will remove the first item from the list which is at index 0
sorted_books.pop(-1) # This will remove the last item in the book. Using the negative one will start at the end of the list.

print(f'\nBook List After Deletions:\n{sorted_books}')

print(f'\nThe number of items in my book list is: {len(sorted_books)}')

if 'Brave New World' in sorted_books:
  print('\nBrave New World is in the list.')
else:
  print('\nBrave new World is NOT in the list.')

#*********************************************************

#****Assignment 1, Part A, Section 3

#*********************************************************

print('\n*********** Section: 3 ***********')

#class Node(object):
#  def __init__(self, data):
#    self.left = None
#    self.right = None
#    self.data = data
#class BinaryTree(object):
#  def __init__(self, root):

#input()