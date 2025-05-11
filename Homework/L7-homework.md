# **Homework 7: Loops in Python**

## **Overview**
This homework will help you **practice** using **for** and **while** loops in Python. You’ll answer a few **theory questions** to ensure you understand loop fundamentals, then tackle **practical coding tasks** involving iteration, condition checks, and loop control statements.

---

## **Part A: Theory Questions**

1. **Comparing Loops**  
   - In your own words, describe the **differences** between a **for** loop and a **while** loop.  
   - Provide one example scenario where you’d prefer a **for** loop and another where you’d choose a **while** loop.

2. **Loop Control**  
   - Explain what the **`break`** and **`continue`** statements do inside a loop.  
   - How does each one affect the flow of the loop?

3. **Range Function**  
   - How does the **`range(start, stop, step)`** function work?  
   - Give an example of generating numbers from 10 down to 1 using `range()`.

---

## **Part B: Coding Exercises**

1. **Even and Odd Checker**  
   - **Task**: Write a program that **iterates** through numbers **1 to 10** and prints whether each number is **even** or **odd**.  
   - **Hint**: Use the **modulus** operator (`%`) and a **for** loop with `range(1, 11)`.

2. **Countdown with `while`**  
   - **Task**: Prompt the user for a **starting number**.  
   - Use a **while** loop to **count down** from that number to **0**, printing each value as you go.  
   - **Hint**: Decrement the number each iteration to avoid an infinite loop.

3. **Sum of Digits**  
   - **Task**: Write a program that takes an **integer** from the user and **calculates the sum of its digits**.  
   - **Hint**: Convert the number to a **string**, iterate through each character, and convert back to an integer to sum. Alternatively, repeatedly use modulus (`% 10`) and integer division (`// 10`) in a `while` loop.

4. **Number Guessing Game**  
   - **Task**: Create a simple **guessing game** with a **secret number**.  
   - Prompt the user to **guess** a number. Provide **feedback** if the guess is too high or too low.  
   - Use a **while** loop to keep asking until the guess is **correct**. Then print a success message.  
   - **Optional**: Limit the number of guesses and end the game if they run out of tries.

5. **Multiples of 3 (with `break`)**  
   - **Task**: Write a `for` loop that prints numbers from **1 to 20**.  
   - If the current number is a **multiple of 3**, **break** out of the loop immediately (don’t print remaining numbers).  
   - **Hint**: Check if a number is a multiple of 3 by using `(number % 3 == 0)`.

---

## **Submission Guidelines**

1. **Theory Answers**:  
   - Write your responses in **clear, concise sentences**.  
   - You can include them as **comments** at the top of your `.py` files or in a separate text file.

2. **Coding Exercises**:  
   - Provide each exercise in its **own `.py` file** or combine them in a single file with **comments** indicating each exercise.
   - Ensure your code is **readable** and **well-commented**.

3. **Testing**:  
   - Run each program to confirm there are **no errors**.  
   - If using **user input**, test with different input values to validate your code’s functionality.

4. **References**:  
   - You may use **class notes**, the official **Python documentation**, or reliable online resources for syntax help.  

---

**Good luck and happy looping!** Use these exercises to strengthen your loop logic and gain confidence in iterating over data. If you have any questions, don’t hesitate to ask your instructor or peers for guidance.