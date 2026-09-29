
# TASK 3 · Random Password Generator

# Objective: Build a Python tool that generates strong, random passwords based on user-defined criteria. Beginners build a command-line version; advanced builds a GUI with complexity controls and clipboard integration.

# Tech Stack — Beginner: Python, random, string Tech Stack — Advanced: Python, secrets (cryptographically secure), tkinter or PyQt5, pyperclip


# Feature Checklist — Beginner Tier:
# [ ] Prompt user to specify desired password length (minimum 8 characters enforced)
# [ ] Prompt user to choose which character types to include: uppercase letters, lowercase letters, numbers, symbols (at least 2 types must be selected)
# [ ] Generate and display a password matching all specified criteria
# [ ] Input validation: reject invalid lengths or no character types selected
# [ ] Option to generate another password without restarting the program




# Self-Sourcing Guideline: Search "Python password generator tutorial random string" on YouTube for the beginner approach. For the advanced tier, search "Python tkinter password generator GUI" and "Python secrets module vs random". Reference the Python documentation for secrets (docs.python.org/3/library/secrets.html) — use it instead of random for anything security-related. For clipboard integration, search "pyperclip Python tutorial".


import random
import string



# 1. CHARACTER SETS


# Uppercase letters: A-Z
uppercase = string.ascii_uppercase

# Lowercase letters: a-z
lowercase = string.ascii_lowercase

# Numbers: 0-9
numbers = string.digits

# Symbols that can be used in the password
symbols = "!@#$%^&*()-_=+[]{};:,.?/<>~"



# 2. ASK HOW MANY CHARACTER TYPES THE USER WANTS


while True:

    try:
        num = int(
            input("Enter how many character types you want to use (2-4): ")
        )

        # Minimum 2 types are required
        if num < 2:
            print("Invalid input!")
            print("Use minimum 2 character types.")
            continue

        # There are only 4 available types
        if num > 4:
            print("Invalid input!")
            print("Use maximum 4 character types.")
            continue

    except ValueError:
        # Handles inputs such as abc, hello, 2.5, etc.
        print("Invalid input!")
        print("Enter numbers only.")
        continue

    # Input is valid, so leave the loop
    break



# 3. FUNCTION TO VALIDATE CHARACTER TYPE


def character_type_valid(prompt):

    while True:

        # Ask the user for a character type
        # .upper() converts u -> U, l -> L, etc.
        ch_type = input(prompt).upper()

        # Only U, L, N and S are allowed
        if ch_type not in ["U", "L", "N", "S"]:
            print("Invalid input!")
            print("U → uppercase")
            print("L → lowercase")
            print("N → numbers")
            print("S → symbols")
            continue

        # Return the valid character type
        return ch_type



# 4. SELECT CHARACTER TYPES


# This list remembers which character types
# the user has already selected.
selected_types = []


print("\n====== CHARACTER TYPE MENU ======")
print("Uppercase = U")
print("Lowercase = L")
print("Numbers   = N")
print("Symbols   = S")


# Repeat according to the number selected by the user
for i in range(1, num + 1):

    while True:

        ch = character_type_valid(
            f"\nChoose character type {i}: "
        )

        # Check whether this type was already selected
        if ch in selected_types:
            print("You already selected this character type.")
            print("Choose a different type.")
            continue

        # Add the new type to the list
        selected_types.append(ch)

        # Leave the duplicate-checking loop
        break


# Display the selected types
print("\nCharacter types selected successfully!")
print("Selected types:", selected_types)



# 5. CREATE THE CHARACTER POOL


# This empty string will contain all characters
# that are allowed in the password.
character_pool = ""


# Add the appropriate character set
# according to the user's choices.

if "U" in selected_types:
    character_pool += uppercase

if "L" in selected_types:
    character_pool += lowercase

if "N" in selected_types:
    character_pool += numbers

if "S" in selected_types:
    character_pool += symbols



# 6. ASK FOR PASSWORD LENGTH


while True:

    try:
        password_length = int(
            input("\nEnter password length (minimum 8): ")
        )

        # Password must contain at least 8 characters
        if password_length < 8:
            print("Password length must be at least 8.")
            continue

    except ValueError:
        print("Invalid input!")
        print("Enter numbers only.")
        continue

    break




# 7. GENERATE PASSWORD


# Start with an empty password
password_characters = []

# Add at least ONE character from every selected type
if "U" in selected_types:
    password_characters.append(random.choice(uppercase))

if "L" in selected_types:
    password_characters.append(random.choice(lowercase))

if "N" in selected_types:
    password_characters.append(random.choice(numbers))

if "S" in selected_types:
    password_characters.append(random.choice(symbols))


# Calculate how many more characters are needed
remaining_characters = password_length - len(password_characters)


# Fill the remaining positions from the combined character pool
for i in range(remaining_characters):
    password_characters.append(random.choice(character_pool))


# Shuffle the characters so the guaranteed characters
# aren't always at the beginning.
random.shuffle(password_characters)


# Convert the list of characters into one password string
password = "".join(password_characters)




# 8. DISPLAY PASSWORD


print("\n================================")
print("Generated Password:", password)
print("================================")



# 9. GENERATE ANOTHER PASSWORD


while True:

    again = input("\nGenerate another password? (Y/N): ").upper()

    if again == "Y":

        password = ""

        # Generate another password
        for i in range(password_length):
            password += random.choice(character_pool)

        print("\nGenerated Password:", password)

    elif again == "N":

        print("\nThank you for using Password Generator!")
        break

    else:

        print("Invalid input!")
        print("Please enter Y or N.")