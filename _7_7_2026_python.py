
#  Dictionary Methods
my_dict = {"name": "Jeni", "age": 22, "course": "IT"}
print(my_dict.keys())       # keys()
print(my_dict.values())     # values()
print(my_dict.items())      # items()
print(my_dict.get("age"))   # get()
my_dict.update({"grade": "A"})  # update()
print(my_dict)

#  List Methods
my_list = [10, 20, 30, 40, 50]
my_list.append(60)          # append()
my_list.remove(20)          # remove()
print(my_list.index(30))    # index()
my_list.sort()              # sort()
my_list.reverse()           # reverse()
print(my_list)

# Tuple Methods
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))    # count()
print(my_tuple.index(3))    # index()
# Tuples are immutable, so only count() and index() are available
# Demonstrating immutability:
try:
    my_tuple[0] = 99
except TypeError:
    print("Tuples are immutable!")

# Set Methods
my_set = {1, 2, 3, 4}
my_set.add(5)               # add()
my_set.remove(2)            # remove()
print(my_set.union({6, 7})) # union()
print(my_set.intersection({3, 4, 8})) # intersection()
my_set.clear()              # clear()
print(my_set)


x = 15

# If
if x > 10:
    print("x is greater than 10")

# If-Else
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# If-Elif-Else
if x < 10:
    print("x is less than 10")
elif x == 15:
    print("x is exactly 15")
else:
    print("x is greater than 10 but not 15")

# Nested If-Else
if x > 10:
    if x < 20:
        print("x is between 10 and 20")
    else:
        print("x is 20 or more")
else:
    print("x is 10 or less")

# Loop Control Statements

# Break
for i in range(1, 6):
    if i == 3:
        break
    print("Break Example:", i)

# Continue
for i in range(1, 6):
    if i == 3:
        continue
    print("Continue Example:", i)

# Pass
for i in range(1, 4):
    if i == 2:
        pass  # placeholder
    print("Pass Example:", i)

# Input Example

user_name = input("Enter your name: ")
print("Hello,", user_name)

# Built-in Functions

nums = [1, 2, 3, 4, 5]
print(range(5))             # range()
print(len(nums))            # len()
print(type(nums))           # type()

# Loops

# For Loop
for i in range(5):
    print("For Loop:", i)

# While Loop
count = 0
while count < 5:
    print("While Loop:", count)
    count += 1