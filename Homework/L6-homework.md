# **Homework 6: Strings in Python**

## **Overview**
This homework will reinforce your understanding of **string operations**, **methods**, and **formatting** in Python. You’ll answer **conceptual questions** and tackle **practical coding** tasks involving string creation, manipulation, and output formatting.

---

## **Part A: Theory Questions**

1. **String Characteristics**  
   - In your own words, explain what **immutability** means for strings in Python.  
   - How does **immutability** affect your approach when you want to modify an existing string?

2. **Common String Methods**  
   - Briefly describe the purpose of **each** of the following methods:  
     - `lower()`  
     - `upper()`  
     - `strip()`  
     - `split()`  
     - `replace()`  
   - Provide a **short example** (one line of code per method) illustrating how each is used.

3. **String Formatting**  
   - Compare **f-strings** with **older formatting techniques** such as `str.format()` or `%` formatting.  
   - What are **two advantages** of using f-strings for formatting text?

---

## **Part B: Coding Exercises**

1. **Problem 1: Greeting and Repetition**  
   - **Task**:  
     1. Prompt the user for their **name**.  
     2. Print a greeting that says, for example, `"Hello, Alice!"`.  
     3. Prompt the user for a **number** (an integer).  
     4. Repeat the greeting message that many times on separate lines.

   > **Hint**: You can use the `*` operator for string repetition, or simply use a loop to print multiple times.

2. **Problem 2: Case Conversion**  
   - **Task**:  
     1. Prompt the user for a **sentence**.  
     2. Print the sentence in **uppercase** and in **lowercase**.  
     3. Remove any leading/trailing spaces and print the **stripped** version.

   > **Hint**: Remember methods like `upper()`, `lower()`, and `strip()`.

3. **Problem 3: Word Counter**  
   - **Task**:  
     1. Prompt the user for a **paragraph** of text (it can be multiple sentences).  
     2. **Split** the paragraph into individual words.  
     3. Print how many words are in the paragraph.  
     4. (Optional) Print the **longest** word in the paragraph.

   > **Hint**: Use `split()` to get a list of words and `len()` to count them. You can also keep track of which word is longest by comparing lengths.

4. **Problem 4: String Search and Replace**  
   - **Task**:  
     1. Prompt the user for a **sentence** and a **target word** to find.  
     2. Print the **index** where that word is found (or a message if it isn’t found).  
     3. Prompt the user for a **replacement word**.  
     4. Print the **updated sentence** after replacing the target word with the replacement word.

   > **Hint**: Use `find()` or `index()` to locate a substring. Remember that `find()` returns `-1` if the substring isn’t found.

5. **Problem 5: Simple Logger (String Formatting)**  
   - **Task**:  
     1. Prompt the user for an **action** (e.g., `"logged in"`, `"started the program"`, etc.).  
     2. Prompt the user for their **username**.  
     3. Print a **formatted** message like `"[INFO] User 'username' performed action at HH:MM:SS"`. Use **f-strings** to format the time or any other details you’d like to include.

   > **Hint**: You can import the `datetime` module to get the current time. For instance:
   ```python
   from datetime import datetime
   current_time = datetime.now().strftime("%H:%M:%S")
   ```
   Then use an f-string to combine everything into a single log message.

---

## **Submission Guidelines**

1. **Answers to Theory**:  
   - Submit your responses in a text file (`.txt` or `.md`) or as comments at the top of your `.py` file(s).

2. **Coding Exercises**:  
   - Provide one `.py` file **per exercise** OR a single `.py` file with clear comment headers (e.g., `# Problem 1`, `# Problem 2`, etc.).  
   - Ensure your code follows **proper Python syntax** and indentation.

3. **Formatting & Comments**:  
   - Include **comments** in your code to explain your logic or any tricky parts.  
   - Make sure each program runs **without errors**.

4. **Reference**:  
   - You may consult **class notes**, the **Python documentation**, or **online resources** for reminders on syntax or methods.

---

**Good luck and happy coding!** Feel free to experiment with additional string methods or formatting features to demonstrate your creativity and deepen your understanding of string handling in Python.