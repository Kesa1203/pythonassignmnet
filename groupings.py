# Empty list
my_list = []
print(my_list)

# Appending items to my_list individually
for item in [10, 20, 30, 40]:
    my_list.append(item)
print("After append:", my_list)

# Inserting a value at a specific index
my_list.insert(1, 15)
print("After insert:", my_list)

# Extending my_list with another list
my_list.extend([50, 60, 70])
print("After extend:", my_list)

#Removing the last element form my_list
my_list.pop()
print("After pop:", my_list)

#Sorting my list in ascending order
my_list.sort()
print("After sort:", my_list)

#locating and printing the index value 30 in my_list
print("Index of 30:", my_list.index(30))
