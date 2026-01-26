# Math module contains many important mathematic constants and functions
import math
import json
import re

# min() and max() functions - find the smallest and largest value in an iterable(collections) or amongst multiple arguements
x = min(2, 7, 99, 18, 4)
y = max(6, 17, 81, 100, 42)

print()
print(f"Minimum value: {x}, Maximum value: {y}")

# abs() function returns the absolute value of a number
z = abs(-7.23)
print()
print(f"Absolute Value: {z}")

# pow() function returns the value of a number raised to the power of another number
a = pow(3, 4) # 3 to the power of 4 (3^4)
print()
print(f"Power of: {a}")

# sqrt() function returns the square root of a number, returns a float
b = math.sqrt(64)
print()
print(f"Square Root: {b:.0f}")

# ceil() function that rounds a number up to the nearest integer
c = math.ceil(4.2)

# floor() functiont that rounds a number down to the nearest integer
d = math.floor(7.8)

print()
print(f"Ceil: {c}, Floor: {d}")

# pi constant represents the mathematical constant pi
p = math.pi

print()
print(f"The value of PI: {p}")


# JSON
# The JSON module can be used to work with JSON data
# JSON stands for JavaScript Object Notation

# We can parse JSON obkects and convert them into Python dictionaries
json_data = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print()
print(f"Name: {data["name"]}")

# we can convert Python dictionaries into JSON objects
# dict, list, tuple, string, int, floats, boolean, None can all be converted to JSON using dumps() function
python_dict = {"fruit": "Apple", "color": "Red", "quantity": 5}
json_object = json.dumps(python_dict)
print()
print(f"JSON Object: {json_object}")

#dumps() function can take additional parameters to format the JSON output
student = {
    "name": "Brandon",
    "id": 12345,
    "courses": {
        "math": {
            "grade": "A",
            "credits": 3
        },
        "python": {
            "grade": "A-",
            "credits": 4
        }
    }
}
formatted_json = json.dumps(student, indent = 4)
print()
print(f"Formatted JSON: {formatted_json}")


# RegEx stands for regular expressions, which is a sequence of characters that forms a search pattern
# Useful for finding substrings, data validation, text manipulation, and more
# The re module provides support for regular expressions in python

#search() function to search for a pattern within a string
text = "The cat and rat are on the roof with another cat eating cat food and wearing 3 shoes and 4 collars"
match = re.search("cat", text)

if match:
    print()
    print(f"Pattern Found: {match.group()}")

# we can use the findall() function to find all occurances of a pattern in a string
matches = re.findall("cat", text)

if matches:
    print()
    print(f"All occurances of 'cat': {matches}")

# regex metacharacters can help us perform more complex searches
# aka wildcards
# [] - help search for a set of characters
print(re.findall(r"[crh]at", text)) # checks for all instances of 'cat' and 'rat'

# \d - search for any digit 0-9
print(re.findall(r"\d", text))

# ^ - string starts with certain character (string)
print(re.search(r"^The", text)) # checks if the string starts with 'The'

# $ - string ends with certain character (string)
print(re.search(r"collars$", text)) # checks if the string ends with 'collars'

# split() function splits a string at each match of a pattern
split_text = re.split(r"\s", "split this text into words.") # using \s lets us split at the spaces
for split in range(len(split_text)):
    print(split_text[split])

# sub() function replaces matches with a specified string
replaced_text = re.sub(r"cat", "dog", text)
print(replaced_text)