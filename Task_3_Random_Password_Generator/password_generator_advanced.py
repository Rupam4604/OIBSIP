# TASK 3 · Random Password Generator

# Objective: Build a Python tool that generates strong, random passwords based on user-defined criteria. Beginners build a command-line version; advanced builds a GUI with complexity controls and clipboard integration.

# Tech Stack — Beginner: Python, random, string Tech Stack — Advanced: Python, secrets (cryptographically secure), tkinter or PyQt5, pyperclip





# Feature Checklist — Advanced Tier (includes all Beginner features, plus):
# [ ] GUI window with sliders or spinboxes for length control and checkboxes for character type selection
# [ ] Use secrets module (not random) for cryptographically secure generation
# [ ] Password strength indicator: display a visual bar or label showing strength (Weak / Medium / Strong) based on length and character diversity
# [ ] Security rules enforced: generated password guaranteed to contain at least one character from each selected type
# [ ] "Copy to Clipboard" button using pyperclip — password copies automatically on generation
# [ ] Option to exclude ambiguous characters (e.g., 0, O, l, 1) via a checkbox
# [ ] Generation history: display the last 5 generated passwords in the session (do not persist to file for security)


# Self-Sourcing Guideline: Search "Python password generator tutorial random string" on YouTube for the beginner approach. For the advanced tier, search "Python tkinter password generator GUI" and "Python secrets module vs random". Reference the Python documentation for secrets (docs.python.org/3/library/secrets.html) — use it instead of random for anything security-related. For clipboard integration, search "pyperclip Python tutorial".


# Import required modules


import tkinter as tk
from tkinter import ttk, messagebox

# secrets is used instead of random because it is designed
# for generating cryptographically secure random values.
import secrets

# string provides ready-made character sets such as:
# uppercase letters, lowercase letters and digits.
import string

# pyperclip allows us to copy the generated password
# directly to the system clipboard.
import pyperclip



# Character sets


# Uppercase English letters: A-Z
UPPERCASE = string.ascii_uppercase

# Lowercase English letters: a-z
LOWERCASE = string.ascii_lowercase

# Numbers: 0-9
NUMBERS = string.digits

# Symbols used by the password generator
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/<>~"



# Ambiguous characters


# These characters can sometimes look similar.
#
# Examples:
# 0 -> zero
# O -> capital O
# l -> lowercase L
# 1 -> one
#
# The user can choose to remove these characters.
AMBIGUOUS_CHARACTERS = "0Ol1"



# Store the last 5 generated passwords


# This list exists only while the application is running.
#
# Passwords are NOT saved to a file or database.
password_history = []



# Create the main Tkinter window


root = tk.Tk()

# Set the title of the application
root.title("Random Password Generator")

# Set the initial window size
root.geometry("600x900")

# Prevent the window from becoming too small
root.minsize(600, 700)



# Create Tkinter variables


# Password length variable
password_length = tk.IntVar(value=12)

# Checkboxes for character types
use_uppercase = tk.BooleanVar(value=True)
use_lowercase = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

# Checkbox for excluding ambiguous characters
exclude_ambiguous = tk.BooleanVar(value=False)

# Variable used to display the generated password
password_display = tk.StringVar()

# Variable used to display password strength
strength_display = tk.StringVar(value="Strength: Not Generated")



# Main title


title_label = ttk.Label(
    root,
    text="🔐 Random Password Generator",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=(20, 10))



# Subtitle


subtitle_label = ttk.Label(
    root,
    text="Generate strong and secure passwords",
    font=("Arial", 11)
)

subtitle_label.pack(pady=(0, 20))



# PASSWORD LENGTH SECTION

length_frame = ttk.LabelFrame(
    root,
    text="Password Length",
    padding=15
)

length_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


# Label showing the current length
length_label = ttk.Label(
    length_frame,
    text="Length:"
)

length_label.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

# Spinbox for password lengt

length_spinbox = ttk.Spinbox(
    length_frame,
    from_=8,
    to=128,
    textvariable=password_length,
    width=10
)

length_spinbox.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


# Information label
length_info = ttk.Label(
    length_frame,
    text="Minimum: 8 characters | Maximum: 128 characters"
)

length_info.grid(
    row=0,
    column=2,
    padx=10,
    pady=5
)

# CHARACTER TYPE SECTIO

character_frame = ttk.LabelFrame(
    root,
    text="Character Types",
    padding=15
)

character_frame.pack(
    fill="x",
    padx=30,
    pady=10
)

# Uppercase checkbo

uppercase_check = ttk.Checkbutton(
    character_frame,
    text="Uppercase Letters (A-Z)",
    variable=use_uppercase
)

uppercase_check.grid(
    row=0,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

# Lowercase checkbo

lowercase_check = ttk.Checkbutton(
    character_frame,
    text="Lowercase Letters (a-z)",
    variable=use_lowercase
)

lowercase_check.grid(
    row=1,
    column=0,
    sticky="w",
    padx=5,
    pady=5
)

# Numbers checkbo

numbers_check = ttk.Checkbutton(
    character_frame,
    text="Numbers (0-9)",
    variable=use_numbers
)

numbers_check.grid(
    row=0,
    column=1,
    sticky="w",
    padx=5,
    pady=5
)


symbols_check = ttk.Checkbutton(
    character_frame,
    text="Symbols (!@#$...)",
    variable=use_symbols
)

symbols_check.grid(
    row=1,
    column=1,
    sticky="w",
    padx=5,
    pady=5
)

# SECURITY OPTION

security_frame = ttk.LabelFrame(
    root,
    text="Security Options",
    padding=15
)

security_frame.pack(
    fill="x",
    padx=30,
    pady=10
)

# Exclude ambiguous characters checkbox

ambiguous_check = ttk.Checkbutton(
    security_frame,
    text="Exclude ambiguous characters (0, O, l, 1)",
    variable=exclude_ambiguous
)

ambiguous_check.pack(
    anchor="w"
)



# PASSWORD DISPLAY SECTION


password_frame = ttk.LabelFrame(
    root,
    text="Generated Password",
    padding=15
)

password_frame.pack(
    fill="x",
    padx=30,
    pady=10
)



# Entry box to display generated password


password_entry = ttk.Entry(
    password_frame,
    textvariable=password_display,
    font=("Consolas", 14),
    justify="center"
)

password_entry.pack(
    fill="x",
    padx=5,
    pady=5
)



# PASSWORD STRENGTH SECTION


strength_frame = ttk.Frame(root)

strength_frame.pack(
    fill="x",
    padx=30,
    pady=5
)



# Strength label


strength_label = ttk.Label(
    strength_frame,
    textvariable=strength_display,
    font=("Arial", 12, "bold")
)

strength_label.pack()



# Strength progress bar


strength_progress = ttk.Progressbar(
    strength_frame,
    orient="horizontal",
    length=400,
    mode="determinate",
    maximum=100
)

strength_progress.pack(
    pady=5
)


# =
# FUNCTION: BUILD CHARACTER POOLS
# =

def get_character_pools():
    """
    Create the character pools based on the selected
    character types.

    Returns:
        selected_pools -> list containing selected character sets
    """

    selected_pools = []

    # Add uppercase characters if checkbox is selected
    if use_uppercase.get():
        selected_pools.append(UPPERCASE)

    # Add lowercase characters if checkbox is selected
    if use_lowercase.get():
        selected_pools.append(LOWERCASE)

    # Add numbers if checkbox is selected
    if use_numbers.get():
        selected_pools.append(NUMBERS)

    # Add symbols if checkbox is selected
    if use_symbols.get():
        selected_pools.append(SYMBOLS)

    return selected_pools


# =
# FUNCTION: REMOVE AMBIGUOUS CHARACTERS
# =

def remove_ambiguous_characters(character_pool):
    """
    Remove characters such as 0, O, l and 1
    when the user selects the security option.
    """

    # Create a new string containing only allowed characters
    filtered_pool = ""

    for character in character_pool:

        # Keep the character only if it is not ambiguous
        if character not in AMBIGUOUS_CHARACTERS:
            filtered_pool += character

    return filtered_pool


# =
# FUNCTION: CALCULATE PASSWORD STRENGTH
# =

def calculate_strength(password, number_of_types):
    """
    Calculate a simple password strength level.

    The strength depends on:
        - Password length
        - Number of character types used

    Returns:
        Weak / Medium / Strong
    """

    length = len(password)

    # Weak password
    if length < 10 or number_of_types <= 1:
        return "Weak"

    # Strong password
    elif length >= 16 and number_of_types >= 3:
        return "Strong"

    # Medium password
    else:
        return "Medium"


# =
# FUNCTION: UPDATE STRENGTH DISPLAY
# =

def update_strength(password, number_of_types):
    """
    Update the strength label and progress bar.
    """

    strength = calculate_strength(
        password,
        number_of_types
    )


    # Weak password


    if strength == "Weak":

        strength_display.set(
            "Strength: Weak"
        )

        strength_progress["value"] = 30



    # Medium password


    elif strength == "Medium":

        strength_display.set(
            "Strength: Medium"
        )

        strength_progress["value"] = 60



    # Strong password


    else:

        strength_display.set(
            "Strength: Strong"
        )

        strength_progress["value"] = 100


# =
# FUNCTION: GENERATE PASSWORD
# =

def generate_password():
    """
    Generate a secure password using secrets.

    The function guarantees that at least one character
    from every selected character type is included.
    """


    # Validate password length


    try:

        # Convert the Spinbox value into an integer
        length = int(password_length.get())

    except (ValueError, tk.TclError):

        messagebox.showerror(
            "Invalid Length",
            "Please enter a valid password length."
        )

        return


    # Password must be at least 8 characters
    if length < 8:

        messagebox.showerror(
            "Invalid Length",
            "Password length must be at least 8 characters."
        )

        return


    # Password maximum length
    if length > 128:

        messagebox.showerror(
            "Invalid Length",
            "Password length cannot exceed 128 characters."
        )

        return



    # Get selected character types


    selected_pools = get_character_pools()



    # At least two character types must be selected


    if len(selected_pools) < 2:

        messagebox.showwarning(
            "Character Types Required",
            "Please select at least two character types."
        )

        return



    # Make sure password is long enough to contain
    # one character from every selected type.


    if length < len(selected_pools):

        messagebox.showerror(
            "Invalid Length",
            "Password length is too short for the selected "
            "character types."
        )

        return



    # Apply ambiguous-character filtering


    if exclude_ambiguous.get():

        filtered_pools = []

        for pool in selected_pools:

            filtered_pool = remove_ambiguous_characters(pool)

            # Make sure the pool is not empty
            if filtered_pool:
                filtered_pools.append(filtered_pool)

        selected_pools = filtered_pools



    # Create one large character pool


    character_pool = ""

    for pool in selected_pools:

        character_pool += pool



    # Generate one character from every selected type
    #
    # This guarantees that every selected character type
    # appears at least once in the password.


    password_characters = []

    for pool in selected_pools:

        secure_character = secrets.choice(pool)

        password_characters.append(
            secure_character
        )



    # Calculate how many additional characters are needed


    remaining_characters = (
        length - len(password_characters)
    )



    # Generate the remaining characters


    for _ in range(remaining_characters):

        secure_character = secrets.choice(
            character_pool
        )

        password_characters.append(
            secure_character
        )



    # Securely shuffle the password characters
    #
    # secrets.SystemRandom() provides secure random
    # operations for cryptographic purposes.


    secure_random = secrets.SystemRandom()

    secure_random.shuffle(
        password_characters
    )



    # Convert the list into a string


    password = "".join(
        password_characters
    )



    # Display the password


    password_display.set(
        password
    )



    # Automatically copy password to clipboard


    try:

        pyperclip.copy(password)

    except Exception:

        messagebox.showwarning(
            "Clipboard Error",
            "Password generated successfully, "
            "but it could not be copied to clipboard."
        )



    # Update password strength


    update_strength(
        password,
        len(selected_pools)
    )



    # Add password to session history


    password_history.insert(
        0,
        password
    )



    # Keep only the latest 5 passwords


    if len(password_history) > 5:

        password_history.pop()



    # Refresh the history display


    update_history()



# FUNCTION: COPY PASSWORD


def copy_password():
    """
    Copy the currently displayed password to clipboard.
    """

    password = password_display.get()

    # Check if there is a password
    if not password:

        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )

        return


    # Copy password to clipboard
    try:

        pyperclip.copy(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )

    except Exception:

        messagebox.showerror(
            "Clipboard Error",
            "Could not copy password to clipboard."
        )



# FUNCTION: UPDATE HISTORY


def update_history():
    """
    Display the last five generated passwords.
    """

    # Delete existing history items
    history_list.delete(
        0,
        tk.END
    )


    # Add each password to the list
    for index, password in enumerate(
        password_history,
        start=1
    ):

        history_list.insert(
            tk.END,
            f"{index}. {password}"
        )



# GENERATE BUTTON


generate_button = ttk.Button(
    root,
    text="🔐 Generate Secure Password",
    command=generate_password
)

generate_button.pack(
    padx=30,
    pady=(15, 5),
    fill="x"
)



# COPY BUTTON


copy_button = ttk.Button(
    root,
    text="📋 Copy to Clipboard",
    command=copy_password
)

copy_button.pack(
    padx=30,
    pady=5,
    fill="x"
)



# PASSWORD HISTORY SECTION


history_frame = ttk.LabelFrame(
    root,
    text="Session History - Last 5 Passwords",
    padding=10
)

history_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=15
)



# Listbox for password history


history_list = tk.Listbox(
    history_frame,
    font=("Consolas", 11),
    height=5
)

history_list.pack(
    fill="both",
    expand=True
)



# SECURITY INFORMATION


security_info = ttk.Label(
    root,
    text=(
        "🔒 Passwords are generated using Python's "
        "secrets module.\n"
        "History is stored only during this session "
        "and is never saved to a file."
    ),
    justify="center",
    font=("Arial", 9)
)

security_info.pack(
    pady=(0, 15)
)



# START THE APPLICATION


root.mainloop()