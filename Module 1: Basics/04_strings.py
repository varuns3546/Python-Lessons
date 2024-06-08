# Strings

# Strings are text enclosed in quotation marks

# Strings can be enclosed with single quotes. double quotes or triple quotes

# Single quotes are the most common syntax. They are useful if the string contains double quotes

'single quotes example'
'"string containing double quotes"'

# Double quotes are useful if the string contains single quotes

'double quotes example'
"'string containing single quotes'"

# You can access characters of a string using indexing
my_string = "Hello, world!"

# The first index of a string is at the index of 0

print(my_string[0]) # displays "H"

print(my_string[7:12]) # displays "world"

# notice print(my_string[7:12]) displays "world" which is contained in indexes 7 through 11
# the Python interpreter will stop displaying text before the ending index

# There are many built-in methods to manipulate strings

# Length of the string
print(len(my_string)) # Output: 13

# Convert to uppercase
print(my_string.upper()) # Output: HELLO, WORLD!

# Convert to lowercase
print(my_string.lower()) # Output: hello, world!

# Replace substring
print(my_string.replace("Hello", "Hi")) # Output: Hi, world!

# Split string into an array
print(my_string.split()) # Output: ['Hello,', 'world!']

# String Operations

# Concatenation is a useful tool to combine multiple strings
string1 = "Hello"
string2 = "World"
print(string1 + " " + string2) # Output: Hello World
# or
print(string1, string2)

# String formatting can be accomplished using formatting in the print command
language = "Python"
name = "Kevin"
print(f"{name} is studying {language}")
# Output: Kevin is studying Python

# Escape Characters

# Escape characters are used to include special characters in a string

# Newline
print("Hello\nWorld")  # Output:
                        # Hello
                        # World

# Tab
print("Hello\tWorld")  # Output: Hello    World

# Backslash
print("This is a backslash: \\")  # Output: This is a backslash: \



