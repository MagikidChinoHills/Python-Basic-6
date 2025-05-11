#question 1

name = input("Enter your name: ")
greeting = f"Hello, {name}!"
num_repetitions = int(input("Enter a number: "))

for _ in range(num_repetitions):
    print(greeting)

#Question 2
sentence = input("Please enter a sentence: ")

uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()
stripped_sentence = sentence.strip()

print("Uppercase:", uppercase_sentence)
print("Lowercase:", lowercase_sentence)
print("Stripped:", stripped_sentence)

#question 3
paragraph = input("Please enter a paragraph of text: ")

words = paragraph.split()
word_count = len(words)

print("Number of words:", word_count)

find_longest = input("Would you like to find the longest word? (yes/no): ").lower()

if find_longest == "yes":
    longest_word = ""
    for word in words:
        # Remove punctuation to accurately compare word lengths
        cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
        if len(cleaned_word) > len(longest_word):
            longest_word = cleaned_word
    if longest_word:
        print("Longest word:", longest_word)
    else:
        print("No words found in the paragraph.")
#Question 4
def word_replace():
  """
  Prompts the user for a sentence, a target word, and a replacement word, then prints the updated sentence.
  """
  sentence = input("Enter a sentence: ")
  target_word = input("Enter the word to find: ")
  replacement_word = input("Enter the replacement word: ")

  try:
    index = sentence.index(target_word)
    print(f"'{target_word}' found at index: {index}")
  except ValueError:
    print(f"'{target_word}' not found in the sentence.")
    return # Exit the function if the word is not found

  updated_sentence = sentence[:index] + replacement_word + sentence[index+len(target_word):]
  print(f"Updated sentence: {updated_sentence}")

if __name__ == "__main__":
  word_replace()

#Question 5
import datetime

# Prompt for action
action = input("Enter the action performed (e.g., logged in, started the program): ")

# Prompt for username
username = input("Enter your username: ")

# Get current time in HH:MM:SS format
current_time = datetime.datetime.now().strftime("%H:%M:%S")

# Print formatted message using f-string
print(f"[INFO] User '{username}' performed {action} at {current_time}")