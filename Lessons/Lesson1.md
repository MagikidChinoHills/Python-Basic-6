## **Lesson 1 (Teacher’s Edition): Introduction to Programming with Python**

### **Lesson Overview**

This lesson provides a **foundation** in Python programming, focusing on:

1. Understanding **what programming** is and why Python is a great first language.
2. **Installing** Python and writing the very first Python program.
3. Using **print statements** and **user input** functions.
4. Discussing **comments** and **basic syntax**.

Below you’ll find **teaching tips**, **hints**, **real-life scenarios**, and **additional exercises** to further engage students.

---

## **Objective**

By the end of this lesson, students should be able to:

1. Understand the **concept** of programming and how it applies to **real-world** tasks.
2. Install and set up **Python** on their computer.
3. Write a **basic program** that prints a message and takes **user input**.
4. **Explain** what comments are and why they’re important.
5. Use **basic arithmetic** in Python to create a simple calculator program.

---

## **1. What is Programming?**

### **Key Teaching Points**

- Emphasize that **programming** is giving **step-by-step instructions** to a computer.
- Computers can’t infer context; they need **explicit** directions.

### **Teacher Tip**

Encourage students to think of programming like **following a recipe**: each step is **precise**, and missing or altering a step changes the outcome.

### **Real-Life Scenario**

Explain how **smartphone apps**, **websites**, and even **microwave ovens** all rely on programmed instructions to run. Show that students already **interact** with programmed devices daily.

---

## **2. Why Python?**

### **Key Teaching Points**

- Python is known for its **clean, readable syntax**.
- Used in **web development**, **data science**, **AI**, **automation**, and beyond.

### **Teacher Tip**

For absolute beginners, highlight that Python’s code reads like **English sentences**, making it less intimidating compared to other languages.

### **Real-Life Scenario**

Mention that **companies** like Google, Netflix, and Instagram use Python in their **tech stacks**, demonstrating its **industry relevance**.

---

## **3. Setting Up Python**

1. **Download** Python from [python.org/downloads](https://www.python.org/downloads/).
2. **Install** on Windows, Mac, or Linux following the site’s instructions.
3. **Verify** the installation by opening a terminal and typing:
   ```bash
   python --version
   ```

### **Teacher Tip**

- Remind students to add Python to the **PATH** during installation on Windows.
- For Mac/Linux, Python often comes preinstalled, but encourage them to **update** to the latest version for consistency.

### **Potential Pitfall**

Some students may install the wrong version (e.g., **2.x** instead of **3.x**). Clarify that most modern applications and tutorials rely on **Python 3**.

---

## **4. Your First Python Program**

1. **Create a File**: `hello_world.py`
2. **Code**:
   ```python
   # This is a comment
   print("Hello, World!")
   ```
3. **Run** in the terminal:
   ```bash
   python hello_world.py
   ```

### **Teacher Tip**

- Have students add a **comment** with their name or the date at the top of the file.
- Encourage them to **experiment** by changing the printed text.

### **Real-Life Scenario**

Compare this simple script to **system scripts** that display messages on websites or run in the background to **automate** tasks—like **sending notifications** or **pop-up greetings** to users.

---

## **5. Comments in Python**

- **Symbol**: `#`
- **Purpose**:
  - Explain code.
  - Temporarily **disable** code lines during debugging.

**Example**:

```python
# This line prints "Hello, World!"
print("Hello, World!")
```

### **Teacher Tip**

Encourage **liberal use** of comments when students start. Emphasize that **clarity** is more important than having a perfectly minimal codebase, especially for beginners.

---

## **6. User Input and Output**

### **Key Teaching Points**

- `input()` collects a **string** from the user.
- `print()` displays output to the console.

```python
user_input = input("Enter your name: ")
print("Hello,", user_input)
```

### **Teacher Tip**

- Point out that `input()` **always returns a string**. For numbers, students will need to **convert** it (e.g., `int(input())` or `float(input())`).

### **Real-Life Scenario**

From **registering** on a website to filling out a **search query** on Google, user input is **everywhere**.

---

## **Example Programs**

### **Example 1: Greeting User**

```python
user_input = input("Enter your name: ")
print("Hello,", user_input)
```

- **Classroom Demo**: Have a volunteer run the code, input their name, and observe the personalized greeting.

### **Example 2: Simple Calculator**

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
```

- **Teaching Tip**: Emphasize type conversion with `float()` for decimals.
- **Practical Spin**: Relate to daily tasks like **budgeting** or **grade calculation**.

---

## **7. Exercises**

1. **Exercise 1: Custom Greeting**

   - Modify “Hello, World!” to print a **custom** greeting message.
   - **Hint**: Encourage them to add **exclamation** or some ASCII art.
2. **Exercise 2: Age to 100**

   - Ask the user for their **current age**.
   - Print how many years until they turn **100**.
   - **Hint**: If a student is 25, they have 75 years to go.
3. **Exercise 3: Simple Calculator**

   - Takes **two numbers** as input.
   - Performs **addition, subtraction, multiplication, division**.
   - Prints results.
   - **Hint**: Show them how to add more operations if time allows.

### **Additional Practice**

- **Exercise 4**: Fahrenheit to Celsius Converter

  - Prompt user for temperature in Fahrenheit.
  - Convert to Celsius using formula: \((F - 32) \times 5/9\).
  - Print the result.
- **Exercise 5**: Story Creator

  - Ask for inputs like name, place, food.
  - Print a short “story” using those inputs.

---

## **8. Conclusion**

Students have now learned to:

1. **Install** Python and write a **basic script**.
2. Use `print()` and `input()` functions to **output** messages and **accept** user data.
3. **Comment** their code for clarity.
4. Understand the **importance** of Python’s readable syntax and how it’s used in **real-world** applications.

Encourage them to **practice** regularly—by tweaking exercises, playing with different data types, or writing **small programs** to solve daily tasks (like a mini budget tracker).

---

## **Vocabulary Words and Definitions**

- **Programming**: Writing instructions a computer can execute to perform tasks.
- **Python**: A high-level language known for its simplicity and vast range of applications.
- **Syntax**: The rules that define how to write and organize Python code.
- **Comment**: A note in the code starting with `#`, ignored by Python’s interpreter.
- **Variable**: A named container to store data.
- **Input**: Data provided by the user or another source (e.g., keyboard input).
- **Output**: Data displayed or returned by a program (e.g., printed text).
- **Data Types**: Classifications of data (e.g., `int`, `float`, `str`) that affect how Python interprets and manipulates values.

---

## **Teacher Resources & Notes**

- **Tips & Tricks**:

  - Demonstrate in front of the class with a **live coding session**. Let them see **errors** and how to fix them.
  - Encourage pair programming or small group work for exercises.
- **Real-World Projects**:

  - Share examples like **Trello** and **Discord bots** that can start with basic inputs/outputs and grow into bigger scripts.
  - Show how Python scripts can automate tasks like **renaming files**, **scraping data** from websites, or **calculating** monthly budgets.
- **Potential Challenges**:

  - Students might forget to **convert** input to `int` or `float`.
  - Make sure to address **division by zero** if they experiment with advanced calculations.

**End of Lesson 1 (Teacher’s Edition)**

*Encourage your students to **keep experimenting** beyond the classroom exercises. The best way to learn coding is by writing more code, making mistakes, and debugging their way to success!*
