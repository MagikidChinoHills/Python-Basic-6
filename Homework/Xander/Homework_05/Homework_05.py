# Creating a list of integers
my_list = [10, 20, 30, 40, 50]
print(f"Initial list: {my_list}")

# Appending new elements
my_list.append(60)
my_list.append(70)
print(f"List after appending 60 and 70: {my_list}")

# Removing an element by value
my_list.remove(30)
print(f"List after removing 30: {my_list}")

# Removing an element by index
removed_element = my_list.pop(1)  # Removes the element at index 1 (which is 20)
print(f"List after removing the element at index 1: {my_list}")
print(f"The removed element was: {removed_element}")

# Accessing an element at a specific index
first_element = my_list[0]
print(f"The first element in the list is: {first_element}")

# Modifying an element at a specific index
my_list[3] = 85  # Change the element at index 3 (originally 70) to 85
print(f"List after modifying the element at index 3: {my_list}")

# Printing the final list
print(f"Final list: {my_list}")


# Creating a tuple of strings
my_tuple = ("apple", "banana", "cherry")
print(f"Initial tuple: {my_tuple}")

# Accessing elements using indexing
first_element = my_tuple[0]
print(f"The first element is: {first_element}")
second_element = my_tuple[1]
print(f"The second element is: {second_element}")

# Attempting to modify an element (this will cause a TypeError)
try:
    my_tuple[1] = "grape"
except TypeError as e:
    print(f"\nError when trying to modify an element: {e}")

# Concatenating two tuples
another_tuple = ("orange", "mango")
combined_tuple = my_tuple + another_tuple
print(f"\nFirst tuple: {my_tuple}")
print(f"Second tuple: {another_tuple}")
print(f"Concatenated tuple: {combined_tuple}")

# Printing the final tuples
print(f"\nFinal first tuple: {my_tuple}")
print(f"Final concatenated tuple: {combined_tuple}")