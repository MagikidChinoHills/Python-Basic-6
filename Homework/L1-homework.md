

# **Homework Assignment: Introduction to Programming with Python**

## **Overview**
In this assignment, you will:

1. Install or verify your **Python** environment is set up correctly.  
2. Write and run **simple Python programs** using `print()` and `input()`.  
3. Practice **commenting** your code for clarity.  
4. Experiment with **arithmetic operations** to build a mini calculator.

---

## **Instructions**

1. **Create a folder** named `lesson1_homework` (or a similar name) to store all your files for this assignment.  
2. For **each exercise**, create a **separate .py file** (e.g., `exercise1.py`, `exercise2.py`, etc.).  
3. **Add comments** at the top of each file explaining what the program does (and optionally, your name and the date).  
4. Test your code by running the `.py` files in the terminal/command prompt.  
5. Submit your `.py` files according to your teacher’s instructions.

---

## **Part A: Basic Python Setup**

1. **Verify Installation**  
   - If you haven’t already, install Python **3.x** from [python.org/downloads](https://www.python.org/downloads/).  
   - Open your terminal and type `python --version` (or `python3 --version` on some systems) to confirm Python is installed.  
   - No file submission required here—just make sure your Python environment works!

---

## **Part B: Simple Programs**

1. **Exercise 1: Hello, World!**  
   - **Filename**: `exercise1.py`
   - **Instructions**:
     1. Write a comment at the top with your name and the purpose of this file.  
     2. Use a `print()` statement to display `"Hello, World!"` (or your own **custom greeting**).  
     3. Save and run your program.  
   - **Example**:
     ```python
     # exercise1.py - Prints a greeting message
     print("Hello, Universe!")
     ```

2. **Exercise 2: Personalized Greeting**  
   - **Filename**: `exercise2.py`
   - **Instructions**:
     1. Ask the user to **enter their name** using `input()`.
     2. Print a **personalized greeting**, like `"Hello, Alice!"`.
   - **Hint**: Remember `input()` returns a string, so you can directly store it in a variable.

3. **Exercise 3: Age to 100**  
   - **Filename**: `exercise3.py`
   - **Instructions**:
     1. Prompt the user for their **current age**.
     2. Calculate how many years until they turn **100**.
     3. Print a message like `"You will be 100 in X years!"`.
   - **Example**:
     ```python
     age = int(input("Enter your current age: "))
     years_to_100 = 100 - age
     print("You will be 100 in", years_to_100, "years!")
     ```

4. **Exercise 4: Simple Calculator**  
   - **Filename**: `exercise4.py`
   - **Instructions**:
     1. Prompt the user for **two numbers** (hint: convert inputs to `float`).
     2. Perform **addition, subtraction, multiplication, and division** on these numbers.
     3. Print the results clearly labeled.
   - **Example**:
     ```python
     num1 = float(input("Enter the first number: "))
     num2 = float(input("Enter the second number: "))

     print("Sum:", num1 + num2)
     print("Difference:", num1 - num2)
     print("Product:", num1 * num2)
     print("Quotient:", num1 / num2)
     ```

---

## **Part C: Additional Challenges (Optional)**

1. **Fahrenheit to Celsius Converter**  
   - Prompt the user for a temperature in Fahrenheit.
   - Convert it to Celsius using the formula \((F - 32) * 5/9\).
   - Print the result.

2. **Story Creator**  
   - Ask for inputs such as a **name**, a **place**, and a **favorite food**.
   - Print a **funny short story** using the collected inputs.

3. **Debugging Practice**  
   - Intentionally create a file (`debug_practice.py`) with a few **errors** (e.g., missing parenthesis, forgetting to convert input to int/float).
   - Try to run the code, observe **error messages**, and **debug** the script until it works.

---

## **Real-World Connection**
- **Personalized greetings** are similar to what **websites** show when you log in (e.g., “Welcome back, John!”).  
- **Calculators** demonstrate how software handles **arithmetic** tasks, akin to budgeting apps or grade calculators used in real-world scenarios.  
- **Converting Fahrenheit to Celsius** mirrors apps like **weather** forecasts or scientific calculations.

---

## **Submission Guidelines**

1. **File Organization**: Ensure you have each exercise in its own `.py` file.  
2. **Code Quality**:  
   - Include **comments** at the top describing the file’s purpose.  
   - Use **clear variable names** and **consistent indentation**.  
3. **Testing**:  
   - Run each `.py` file to confirm it behaves as expected (no syntax errors).  
   - Consider edge cases (e.g., division by zero in your calculator, negative ages).  
4. **Submission**:  
   - Zip your `lesson1_homework` folder or upload each `.py` file according to your teacher’s instructions.  

---

## **Grading / Evaluation**

- **Completeness**: Did you finish all **required** exercises (Exercises 1–4)?  
- **Functionality**: Do your programs run without errors?  
- **Clarity**: Are your **comments** and **variable names** descriptive?  
- **Creativity** (Optional): Did you attempt any **additional challenges**?

---

## **Happy Coding!**

As you work through these exercises, remember that **practice** is the best way to learn. Don’t be afraid to **experiment**, **debug**, and explore Python’s features! If you encounter any issues, refer back to your lesson notes or ask your teacher for help.