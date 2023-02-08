# variables
first = 'shubham'
last = 'Kunar'
# Receiving Input
birth_year = int(input('Birth year: '))
print(f'My name is {first[0:-2]} {last}.')  # formatted string
print("My year of birth is " + str(birth_year))
print(f'length of string is: {len(first)}')
print(first.upper())
print(last.replace('n', 'm', 1))
print(first.title())
# Arithmetic Operations
# +
# -
# *
# /  returns a float
# //  returns an int
# %  returns the remainder of division
# **  exponentiation - x ** y = x to the power of y

# if else
is_hot = False
if is_hot:
    print("It's a sunny day")
else:
    print("Go play outside")
    print("return home")

# while loop
i = 1
while i < 5:
    print(i*"@")
    i += 1

# For loops
for i in range(1, 5):
    print(i)
#  range(5): generates 0, 1, 2, 3, 4
#  range(1, 5): generates 1, 2, 3, 4
#  range(1, 5, 2): generates 1, 3
