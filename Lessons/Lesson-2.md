Lesson 2 (Teacher’s Edition): Variables and Data Types in Python
Lesson Overview
In this lesson, students learn about variables—how to create, name, and assign values to them. They also explore data types (integers, floats, strings, and booleans), perform simple operations, and see how to use these types in practice. This teacher’s edition includes teaching tips, examples, and solutions for the exercises.

Objective
By the end of this lesson, students will be able to:

Understand what variables are and how to name them properly in Python.
Identify and work with core data types (int, float, str, and bool).
Perform basic arithmetic and string manipulations.
Create and execute short Python scripts that store and manipulate data.
1. Introduction to Variables
Key Teaching Points
A variable is a named container in Python that holds a value.
Variables let us reuse data (like a user’s name) throughout our program.
Teacher Tip
Emphasize that students can reuse variables in multiple places without rewriting the value.
Real-Life Analogy
Compare a variable to a labeled box in a warehouse; the label is the variable name, and the item inside is the value stored.
2. Naming Variables
Rules & Best Practices
Must start with a letter or underscore (_), followed by letters, digits, or underscores.
Case-sensitive: userAge ≠ userage.
Pick descriptive names for clarity.
my_variable = 42
name = "Alice"
is_student = True
temperature = 25.5
Teacher Tip
Demonstrate bad naming: x, a1, var2, so students see why descriptive names (e.g., user_name) are better.
3. Data Types in Python
Common Data Types
Integer (int)

Whole numbers (e.g., 42, -10, 0).
Example: students_count = 20
Float (float)

Numbers with decimal points (e.g., 3.14, -0.5).
Example: price = 9.99
String (str)

Text in quotes (e.g., "Hello", 'World').
Example: greeting = "Hello, everyone!"
Boolean (bool)

Only True or False.
Example: is_logged_in = False
Teacher Tip
Encourage experimentation with the type() function:
print(type(price))  # <class 'float'>
Real-Life Scenarios
Integer for counting (e.g., number of books).
Float for measurements (e.g., temperature).
String for text (e.g., names).
Boolean for yes/no decisions (e.g., user is logged in or not).
In-Class Examples
Example 1: Integer Operations
num1 = 10
num2 = 5

# Addition
sum_result = num1 + num2
print("Sum:", sum_result)

# Subtraction
difference_result = num1 - num2
print("Difference:", difference_result)

# Multiplication
product_result = num1 * num2
print("Product:", product_result)

# Division
quotient_result = num1 / num2
print("Quotient:", quotient_result)
Teaching Tip: Show that // (integer division) rounds down.

Example 2: Float Operations
pi = 3.14159
radius = 2.0

# Calculate the area of a circle
area = pi * (radius ** 2)
print("Circle Area:", area)
Teaching Tip: Demonstrate ** is for exponentiation (e.g., radius ** 2 means radius squared).

Example 3: String Operations
first_name = "John"
last_name = "Doe"

# Concatenate strings
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# String length
name_length = len(full_name)
print("Name Length:", name_length)
Teaching Tip: Students can try .upper() or .lower() to transform strings.

Example 4: Boolean Logic
is_python_fun = True
is_learning = False

# Logical AND
both_conditions = is_python_fun and is_learning
print("Both Conditions:", both_conditions)

# Logical OR
either_condition = is_python_fun or is_learning
print("Either Condition:", either_condition)

# Logical NOT
not_python_fun = not is_python_fun
print("Not Python Fun:", not_python_fun)
Teaching Tip: Ask students to guess the outputs before running the code.

4. Exercises
Exercise 1

Create a variable my_age and assign your age (integer).
Exercise 2

Create a variable favorite_number and assign your favorite number (float).
Exercise 3

Create a variable greeting and assign it a string with a friendly greeting.
Exercise 4

Create a variable is_happy and assign it a boolean (True or False).
Exercise 5

Calculate the sum of two integers and store the result in total.
Exercise 6

Concatenate two strings (first name and last name) to form full_name.
Exercise 7

Calculate the average of two float numbers and store the result in average.
5. Conclusion
Variables and data types form the foundation of Python programming. By mastering them, students can tackle more complex tasks, from mathematical operations to string manipulation and logical decision-making.

Encourage students to play around with these concepts outside the classroom—creating mini-programs, exploring new data types, and practicing arithmetic and string operations on their own.

Vocabulary Words and Definitions
Variable: A named space in memory to store data.
Data Types: Categories (like int, float, str, bool) that define how data is stored and manipulated.
Integer (int): A whole number (e.g., 42, -10).
Float (float): A decimal number (e.g., 3.14).
String (str): A sequence of characters in quotes (e.g., "Hello").
Boolean (bool): A True/False value used in logical expressions.
Concatenation: Linking strings end-to-end (e.g., "Hello" + " " + "World").
Type Casting: Converting data from one type to another (e.g., float("10") → 10.0).
Exercise Solutions
Below are sample solutions for the exercises. Encourage students to try their own approaches before showing them these solutions!

Exercise 1
my_age = 25  # Replace 25 with actual age
print("My age is", my_age)
Exercise 2
favorite_number = 7.5  # Example favorite float number
print("My favorite number is", favorite_number)
Exercise 3
greeting = "Hello, everyone!"
print(greeting)
Exercise 4
is_happy = True
print("Am I happy?", is_happy)
Exercise 5
num1 = 10
num2 = 20
total = num1 + num2
print("The total is", total)
Exercise 6
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print("Full name:", full_name)
Exercise 7
number1 = 3.5
number2 = 2.5
average = (number1 + number2) / 2
print("The average is", average)
End of Lesson 2 (Teacher’s Edition)

Encourage students to build short scripts combining these exercises (e.g., taking user input, storing that in variables, performing arithmetic, etc.). Through repetition and experimentation, they’ll gain a deeper comfort with variables and data types—a key stepping stone to more advanced Python concepts!
