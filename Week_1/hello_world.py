# Day 1 - 1/20/2026

print('Hello Word!')
print("Hello World!!!")

## Datatypes in Python

#Variables can be decalred inplicitly without specifying datatype

a = "string of words and characters and yada yada"
explicitString: str = "my explicit string"

#Number types
#Integers - int - whole numbers
b = 7

explicitInt: int = 7

#Float - float - decimal values
c = 3.14159
explicitFloat: float = 3.14159

#Boolean - True/False
#Falsey values: 0, 0.0, empty string "", empty list [], empty tuple (), empty dict {}
#Truthy values: anything else

d = True
explicitBool: bool = False

if b:
    print("b is true")
else:
    print("b is false")

#NoneType - None - represents a null value or the absence of a value
e = None
explicitNone: None = None


#print multiple vairables
print(a, b)

#print sum of b and c
print(b + c)

#mix data types
print("I have", b, "cats in my house")

f = 74
print(f)

f = "Green"
print(f)

#Casting lets us specify the datatype we want to convert to
a = str(9)
b = int(9)
c = float(9) #will print as 9.0
d = bool(9) #will print as True

print(a, b, c, d)

#Check datatypes using the type() function

print(type(a), type(b), type(c), type(d))

#Variables are case sensitive
A = "Uppercase A"
print(A)
a = "lowecase a"
print(a)

#We can assign multiple variables in one line
dog = DOG = Dog = dOg = "Beagle"

print(dog, DOG, Dog, dOg)

# ======= Day 2 of Training =======

#Collections - variables hold multiple values
#Collections is a module in python
# Lists, Tuples, Sets, Dictionaries

"""List is a collection that is ordered and changeable and allows duplicate values
Tuple is a collection that is ordered, unchangeable, and allows duplicate values
Set is a collection that is unordered, unchangeable, and unindexed. Do not allow duplicate values
Dictionary is a collection that is ordered, changeable, and does not allow duplicate values"""

# Lists use square [] brackets and can contain different data types
# Python sees lists as objects with the data type 'list'
fruits = ["Orange", "Strawberry", "Apple"]
fruityFruits = favoriteFruits = ["Strawberry", "Apple", "Banana"]
Or, St, Ap = fruits

print(Or, St, Ap)

mixedTypes = ["cheese", 17, False, 32.7]

#len() returns the lenth of the list
print(len(fruits))

#type() returns the data type of the list
print(type(fruits))

#access and item in the list using the item's index
print(fruits[1])

#We can also use negative indexing which starts from the end
print(fruits[-1])

#We can also access a range of indexes
print(fruits[1:3])

#add items to a list
fruits.append("Grapes")
print(fruits)

#add items at a specific index
fruits.insert(2, "Kiwi")
print(fruits)


#Tuples
#Tuples can contain different data types and are defined as the objects of the data type 'Tuple'
animalTuple = ("Cat", "Dog", "Bird", "Fish")
print(animalTuple)

#len() works for Tuples too
print(len(animalTuple))

#Since tuples are immutable(unchangeable) we cannot use the append() function
#instead we can convert it to a list
animalList = list(animalTuple)
animalList.append("Snake")
print(animalList)


#Sets
#Sets are created using curly braces{}
colorsSet = {"Blue", "Green", "Pink", "Orange"}

#Sets can use the add() and remove() functions for adding and removing elements
colorsSet.add("Brown")
colorsSet.remove("Orange")

print(colorsSet)

#Sets support intersection, difference, and union
secondSet = {"Burger", "Fries", "Milkshake", "Pink", "Brown"}

intersectionSet = colorsSet & secondSet
print("Intersection Set:", intersectionSet)

differenceSet = colorsSet - secondSet
print("Difference Set:", differenceSet)

unionSet = colorsSet | secondSet
print("Union Set:", unionSet)

#Dictionary
#Dictionaries are defined as key-value pairs with curly braces and separated by a colon :
#Pairs are separated by commas ,
#First value is treated as the key and the second is treated as the value
foodDictionary = {
    "Sushi": "Fish",
    "Burger": "Beef",
    "Pizza": "Pepperoni",
}

#values() will return a list of all values in the dictionary
print(foodDictionary.values())
print(foodDictionary.keys())

#the value of a specific item can be changed by referring to its key
foodDictionary["Sushi"] = "Rice"
print(foodDictionary)

#We can also add items by using a new index key and giving it a value
foodDictionary["Pickle"] = "Cucumber"
print(foodDictionary)

#We can check if a key exists in the dictionary
if "Burger" in foodDictionary:
    print("Yes there is a Burger in the Dictionary")
else:
    print("No, no Burger in Dictionary")


#Operators
#Symbols that define operation behaviors between data types

#Arithmatic Operators
# +, -, *, /, %(modulator), **(Exponent), //(Floor Division)

print(11 + 9)
print(19 * 3)

#Assignment Operators
# =, +=, -=, *=, /=, etc...

#Comparison Operators
# ==, !=, >, <, >=, <=

#Logical Operators
# and, or, not


#Getting User Input using the input() function
print("Please enter your name")
name = input()

#f stands for formatted string
#allows us to paramaterize our string
print(f"Hello {name}!")

favColor = input(f"What is your favorite color {name}? ")
print(f"I like {favColor.lower()} too")