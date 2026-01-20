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