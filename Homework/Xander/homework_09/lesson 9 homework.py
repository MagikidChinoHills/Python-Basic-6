#List: An ordered collection of values that can be modified (mutable).

#Example:

#Python

fruits_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
#Tuple: An ordered collection of values that is immutable (cannot be changed after creation).

#Example:

#Python

colors_tuple = ("red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white")
#Dictionary: A collection of key-value pairs for efficient data retrieval.

Example:

Python

student = {"name": "Alice", "age": 25, "major": "Computer Science", "id": "12345"}
#Set: A collection of unique elements used for deduplication and membership testing.

Example:

Python

unique_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}



# Basic Problems Creating Lists and Tuples
favorite_foods = ["pizza", "tacos", "ice cream", "sushi", "pasta"]
favorite_colors = ("blue", "green", "red", "purple", "orange")

print("My favorite foods:", favorite_foods)
print("My favorite colors:", favorite_colors)

# Accessing and Modifying Lists
favorite_foods[1] = "burritos"  # Modify the second element
favorite_foods.append("chocolate") # Add a new food item

print("Modified favorite foods:", favorite_foods)

# Accessing Tuple Elements
last_color = favorite_colors[-1]
print("The last color in my favorite colors tuple is:", last_color)

# Creating a Dictionary
my_info = {
    "Name": "Alice",
    "Age": 30,
    "Favorite Hobby": "Reading"
}

print("My information:", my_info)

# Set Operations
odd_numbers = {1, 3, 5, 7, 9}
multiples_of_3 = {3, 6, 9}

union_set = odd_numbers.union(multiples_of_3)
intersection_set = odd_numbers.intersection(multiples_of_3)
difference_set = odd_numbers.difference(multiples_of_3)

print("Odd numbers:", odd_numbers)
print("Multiples of 3:", multiples_of_3)
print("Union of sets:", union_set)
print("Intersection of sets:", intersection_set)
print("Difference of sets (odd_numbers - multiples_of_3):", difference_set)

# List Manipulation:
numbers = list(range(1, 11)) # Create a list of integers from 1 to 10
print("Original list:", numbers)

# Remove all even numbers from the list
# We iterate backwards or create a new list to avoid issues with modifying while iterating
# Option 1: Using a new list (more Pythonic)
updated_numbers = [num for num in numbers if num % 2 != 0]
numbers = updated_numbers # Update the original list reference
print("Updated list (odd numbers only):", numbers)

# Option 2: Iterating backwards (less common for this specific task)
# for i in range(len(numbers) - 1, -1, -1):
#     if numbers[i] % 2 == 0:
#         numbers.pop(i)
# print("Updated list (odd numbers only, using pop):", numbers)


# Tuple Unpacking:
cities_tuple = ("New York", "Los Angeles", "Chicago", "Houston")
city1, city2, city3, city4 = cities_tuple
print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)
print("City 4:", city4)

# Dictionary Iteration:
country_capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}
print("Country-Capital Pairs:")
for country, capital in country_capitals.items():
    print(f"{country}: {capital}")

# Set Membership Testing:
fruits_set = {"apple", "banana", "cherry", "grape", "orange"}

user_fruit = input("Enter a fruit name to check: ").lower() # Convert to lowercase for case-insensitive check

if user_fruit in fruits_set:
    print(f"Yes, {user_fruit} is in the fruit set.")
else:
    print(f"No, {user_fruit} is not in the fruit set.")