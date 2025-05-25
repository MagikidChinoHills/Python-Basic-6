# Homework Assignment: Python Data Structures

---

## **Section 1: Vocabulary and Definitions**

Provide definitions for the following terms, and include an example for each:

1. **List**: An ordered collection of 10 values that can be modified (**mutable**).
   - Example:
     ```python
     fruits_list = ["apple", "banana", "cherry"]
     ```

2. **Tuple**: An ordered collection of 10 values that is immutable (cannot be changed after creation).
   - Example:
     ```python
     colors_tuple = ("red", "green", "blue")
     ```

3. **Dictionary**: A collection of key-value pairs for efficient data retrieval.
   - Example:
     ```python
     student = {"name": "Alice", "age": 25}
     ```

4. **Set**: A collection of unique elements used for deduplication and membership testing.
   - Example:
     ```python
     unique_numbers = {1, 2, 3}
     ```

---

## **Section 2: Practice Problems**

### **Basic Problems**

1. **Creating Lists and Tuples**:
   - Create a list of your favorite foods and a tuple of your favorite colors. Print both.

2. **Accessing and Modifying Lists**:
   - Modify the second element of the list you created above. Add a new food item to the end of the list.

3. **Accessing Tuple Elements**:
   - Retrieve and print the last element of the tuple you created.

4. **Creating a Dictionary**:
   - Create a dictionary with keys for "Name," "Age," and "Favorite Hobby." Assign values to these keys.

5. **Set Operations**:
   - Create two sets of numbers: one with odd numbers from 1 to 10, and one with multiples of 3 from 1 to 10. Perform and print the union, intersection, and difference of these sets.

---

## **Section 3: Intermediate Problems**

1. **List Manipulation**:
   - Write a program to:
     - Create a list of integers from 1 to 10.
     - Remove all even numbers from the list.
     - Print the updated list.

2. **Tuple Unpacking**:
   - Given the tuple `("New York", "Los Angeles", "Chicago", "Houston")`, unpack the values into four variables and print them.

3. **Dictionary Iteration**:
   - Create a dictionary of three items: the keys should be the names of three countries, and the values should be their capitals. Iterate through the dictionary and print each country-capital pair.

4. **Set Membership Testing**:
   - Write a program to:
     - Create a set of fruits (e.g., `{"apple", "banana", "cherry"}`).
     - Take user input for a fruit name.
     - Check if the fruit is in the set and print an appropriate message.

---

## **Section 4: Advanced Problems with Hints and Tips**

### Problem 1: Frequency Count

**Task**:
Write a program that counts and prints the frequency of each character in a given string.

**Example**:
Input: `"hello world"`

Output:
```
h: 1
e: 1
l: 3
o: 2
w: 1
r: 1
d: 1
```

**Hint**:
- Use a dictionary to store the character as the key and its count as the value.
- Iterate through the string and update the dictionary.

### Problem 2: Dictionary from Lists

**Task**:
Create a dictionary from two lists: one containing names and the other containing scores.

**Example**:
Input:
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
```

Output:
```python
{ "Alice": 85, "Bob": 90, "Charlie": 95 }
```

**Hint**:
- Use the `zip()` function to pair elements from both lists.
- Convert the zipped object into a dictionary using `dict()`.

### Problem 3: Removing Duplicates

**Task**:
Write a program to remove duplicates from a list while maintaining the order.

**Example**:
Input: `[1, 2, 2, 3, 4, 4, 5]`

Output:
`[1, 2, 3, 4, 5]`

**Hint**:
- Use a set to check for duplicates.
- Iterate through the list and add elements to a new list only if they are not in the set.

### Problem 4: Set Operations

**Task**:
Write a program to compare two lists and print the common elements, elements unique to the first list, and elements unique to the second list.

**Example**:
Input:
```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
```

Output:
```
Common: [3, 4]
Unique to list1: [1, 2]
Unique to list2: [5, 6]
```

**Hint**:
- Convert the lists to sets and use intersection, difference, and union operations.

---

## **Section 5: Links to Additional Help**

- [Python Official Documentation: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python: Python Data Structures](https://realpython.com/python-data-structures/)
- [W3Schools: Python - Lists, Tuples, Dictionaries, Sets](https://www.w3schools.com/python/python_lists.asp)

---

## **Happy Coding!**

Complete this assignment to solidify your understanding of Python’s core data structures. Good luck!

