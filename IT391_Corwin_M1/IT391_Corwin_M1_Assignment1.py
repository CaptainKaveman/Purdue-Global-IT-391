#*********************************************************

#****Assignment 1, Section 1

#*********************************************************

print('\n********** Section 1 **********\n')

def Fibonacci(n):

  # Adding an if statement to add redundancy to the function to prevent any numbers that are less than zero.
  if n < 0:
    return "Invalid number"

  # If statement to determine if the number entered is the first or second number in the Fibonacci sequence. If it is the first or second number then it will return n.
  if n in {0, 1}:
    return n

  # Return recursive Fibonacci value for n.
  return Fibonacci(n - 1) + Fibonacci(n - 2)

print(f"The Fibonacci value of 10 is: {Fibonacci(10)}\n")

# Print statement to print a range of numbers in the Fibonacci sequence. Not required, just adding for fun and future use.
#print(f"\n{[Fibonacci(n) for n in range(10)]}")

#*********************************************************

#****Assignment 1, Section 2

#*********************************************************

print('\n********** Section 2 **********\n')

# Function to calculate the factorial value of a number
def factorial(n):
  # If statement to check if the number is a 0 or 1, then the factorial value will equal 1.
  if (n == 0 or n == 1):
    return f'{n}! = {int(1)}'
  # Else statement to calculate the factorial value of any number greater than 1.
  else:
    fact = 1
    for i in range(1, n + 1):
      fact = fact * i
    return f'{i}! = {fact}'

# For loop to calculate the factorial value of the numbers 1 to 4.
for i in range(1, 5):
  print(factorial(i))

# Input request to keep the console window running until the user quits the program.
input('\nPress enter to close . . .')