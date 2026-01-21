import Functions

print(Functions.myCat)

#Control flow statements in Python

#For
loopPets = ["Fluffy", "Wonton", "Ash", "Wontina", "Wontessa"]

#for loops loop through a collection of items
# for x in collection, do something

for pet in loopPets:
    print(pet)

#While
#good for execution while a condition is true
count = 0
while count < 5:
    print("Inside the While Loop")

    # += is the shorthand for count = count + 1
    count += 1

#We can nest loops and mix and match them
#BUT, if you find yourself using 3 or more loops deep, there is likely a better way

#If-else

#We can check a condition or condition(s) and execute a block of code based ont he output(true/false)
#becareful! Python relies on indentation to know where the blocks of code end
cheese = 4
if cheese > 5:
    print("Cheese is the greatest")
else:
    print("Cheese is not the greatest")

#we can check multiple conditions using elif
#this will execute the first true block and skip the rest
#good for checking multiple MUTUALLY EXCLUSIVE conditions
score = 33

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else: #else catches anything that is not caught by previous conditions
    print("Grade F")

#shorthand if
a = 11
b = 9
c = 70

if a > b: print("A is greater than B")
print("A is my favorite") if a > b else print("B is my favorite")

#mutliple conditions using our logical operators
if a > b and c > a:
    print("both conditions are true")
if a > b or c < a:
    print("At least one condition is true")
if not a < b:
    print("a is not less than b")

if a > 5:
    print("A is more than 5")
    if a > 10:
        print("and more than 10")
    else:
        print("but not more than 10")

#Match-case (known as swtich statements in other languages)
choice = input("Select a number between 1 and 3: ")

match choice:
    case "1":
        print("You chose case number 1")
    case "2":
        print("You chose case number 2")
    case "3":
        print("You chose case number 3")
    case _: #this is the default case if none of the above cases are true
        print("You did not follow directions")