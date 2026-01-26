import os #module needed to delete a file

#File handling refers to the process of creating, opening, reading,
#writing, and deleting files using python
#Python has built-in function and methods that make this easy

#Important to know for data persistence and processing
#automation of many real-world tasks
#handling large data sets

#open() - is the key function and takes 2 parameters: filename and mode
# 4 different modes available:
# "r" - read; the default mode for reading and throws an error if the file does not exist
# "a" - append the end of a file and it creates the file if it does not exist
# "w" - write and if a file already has data it will be overwritten
# "x" - create; returns an error if the file fails to create

#we can determine if the file should be handled as binary or text using "b" and "t" respectively

# myFile = open("./Week_1/Resources/MyNewFile.txt", "x") #created our new file
# mySecondFile = open("./Week_1/Resources/MySecondFile.txt", "+w")

myFile = open("./Week_1/Resources/MyNewFile.txt", "r")
# print(myFile.read())

#read a single line, calling it again will read the next line
# print(myFile.readline())
# print(myFile.readline())
# print(myFile.readline())

#we can also specify to only read the x numbers of characters
#Read functions also keep track of where we are
# print(myFile.read(3))
# print(myFile.read(4))

#It is best practice to close a file once we are done with it
# myFile.close()

#We can access files using exact paths
#we can use the "with" statement to automatically close the file after its suite finishes
# with open("C://Users/Brandon Mihalko/OneDrive/Documents/Revature Information/TRNG2364---Data-Foundations-Notes/Week_1/Resources/MyNewFile.txt", "r") as myFile:
#     print(myFile.read())

# print(myFile.read())

# pokemonTeam = []

# for p in range(6):
#     pokemon = input("Enter a pokemon for your team: ")
#     pokemonTeam.append(pokemon)

# with open("./Week_1/Resources/MyPokemonTeam.txt", "+w") as teamFile:
#     for p in pokemonTeam:
#         teamFile.write(p + "\n")
#     print("Your Pokemon team has been saved!")

# with open("./Week_1/Resources/MyPokemonTeam.txt", "r") as teamFile:
#     print("Your pokemon team consists of: ")
#     print(teamFile.read())

#It is best practice to check if a file exists before trying to delete it
if os.path.exists("./Week_1/Resources/MySecondFile.txt"):
    os.remove("./Week_1/Resources/MySecondFile.txt")
    print("File deleted successfully")
else:
    print("Something went wrong, file was not deleted")