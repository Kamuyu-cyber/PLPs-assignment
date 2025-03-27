# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position
my_list.insert(1, 15)
print("My list after inserting 15:", my_list)
# Extend the list with another list
my_list.extend([50, 60, 70])
print("My list after extending:", my_list)
# Remove the last element
my_list.pop()
print("My list after removing the last element:", my_list)
# Sort the list in ascending order
my_list.sort()
print("My list after sorting:", my_list)
# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)