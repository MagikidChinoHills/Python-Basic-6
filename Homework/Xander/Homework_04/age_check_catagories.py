def categorize_age():
  """Categorizes a user's age into Child, Teenager, Adult, or Senior."""
  try:
    age_str = input("Please enter your age: ")
    age = int(age_str)

    if 0 <= age <= 12:
      category = "Child"
    elif 13 <= age <= 19:
      category = "Teenager"
    elif 20 <= age <= 59:
      category = "Adult"
    elif age >= 60:
      category = "Senior"
    else:
      category = "Invalid age"

    if category != "Invalid age":
      print(f"You are categorized as a {category}.")
    else:
      print("Invalid age entered. Please enter a non-negative number.")

  except ValueError:
    print("Invalid input. Please enter a whole number for your age.")

if __name__ == "__main__":
  categorize_age()