# In Python we can have NAMED tuples
# They allow you to access their elements by name and index
# Named tuples are part of the collections module and provide a way to create self documenting, immutable data structures
# Good for reading an object or rows from SQL queries, CSVs, or API responses

from collections import namedtuple, OrderedDict, Counter

# to create a NAMED tuple, we use the namedtuple() factory fucntion
Point = namedtuple('Point', ['pizza', 'y'])

# We can create an instance of Point
p = Point(pizza = 1, y = 5)

# Access using a field name
print(p.pizza, p.y)

# Access items using index
print(p[0])

# Acces using a getattr()
print(getattr(p, 'y'))

# more precise example
User = namedtuple('User', ['id', 'username', 'password', 'email'])

myUser = User(
    12,
    'JohnDoe',
    'password',
    'johndoe@email.com',
)

mySecondUser = User(
    88,
    'Jane',
    'something',
    'janesemail@email.com'
)

print(myUser.username, myUser.password, mySecondUser.username, mySecondUser.password)
print()



# Ordered Dictionaries
# are good for when you are using items in a specific order
# great for configuration settings or environment variables
# also from the collections module

config = OrderedDict()

# set defaults
config["timeout"] = 5
config["retries"] = 3
config["two-factor"] = True

# we can override values that are already set
config["timeout"] = 10

# Set certain items to always be considered last
config.move_to_end("timeout")

# we can actually inspect the order
for key, value in config.items():
    print(key, value)

print()



# Counters
# counters allows us to count things without writing loops
# comes from collections module

words = ["Fruit", "Meat", "Veggies", "Dairy", "Grains", "Legumes", "Fruit", "Fruit", "Dairy"]
count = Counter(words)

# Shows count for the whole list, if words appear more than once it +1 to count
print(count)

# Prints the count of what we want from the list
print(count["Fruit"])