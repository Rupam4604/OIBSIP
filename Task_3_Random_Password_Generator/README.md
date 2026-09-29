#  Random Password Generator

A Python-based Random Password Generator developed as part of my **Oasis Infobyte Python Programming Internship (OIBSIP)**.

This project generates random and customizable passwords based on the character types selected by the user.

---

##  Internship Task

**Internship:** Python Programming Internship  
**Organization:** Oasis Infobyte  
**Task:** Task 3 – Random Password Generator  
**Level:** Beginner  
**Language:** Python

---

##  Objective

The objective of this project is to create a command-line password generator that allows users to:

- Select the number of character types to use.
- Choose uppercase letters, lowercase letters, numbers, and symbols.
- Specify the desired password length.
- Generate a random password.
- Generate another password without restarting the program.

---

##  Features

### Character Type Selection

The user can select between **2 and 4 character types**:

| Input | Character Type |
|------|----------------|
| `U` | Uppercase letters |
| `L` | Lowercase letters |
| `N` | Numbers |
| `S` | Symbols |

Lowercase inputs are also accepted automatically.

For example:

```text
u → U
l → L
n → N
s → S
```

##  Input Validation

The program validates user input and prevents:

- Invalid character types
- Duplicate character type selections
- Less than 2 character types
- More than 4 character types
- Non-numeric input where numbers are required
- Password lengths below 8 characters

###  Random Password Generation

The program uses Python's built-in random module to randomly select characters from the selected character pools.

The generated password contains at least one character from every selected character type.

For example, if the user selects:

```text
U + L + N
```

the generated password will contain at least:

1 uppercase letter
1 lowercase letter
1 number

The remaining characters are selected randomly from the combined character pool.

###  Generate Another Password

After generating a password, the user can choose:

Y → Generate another password
N → Exit

The program continues running until the user chooses to exit.

### Technologies Used

- Python
- random module
- string module

### Project Structure

```text
Task_3_Random_Password_Generator/
│
├── password_generator_beginner.py
└── README.md
```
### How to Run

1. Make sure Python is installed

- Check your Python installation:

```text
 python --version
 ```

2. Open the project folder

```text
cd Task_3_Random_Password_Generator
```

3. Run the program
```text
python password_generator_beginner.py
```

### Example
```
Enter how many character types you want to use (2-4): 3

====== CHARACTER TYPE MENU ======
Uppercase = U
Lowercase = L
Numbers   = N
Symbols   = S

Choose character type 1: U
Choose character type 2: L
Choose character type 3: N

Character types selected successfully!
Selected types: ['U', 'L', 'N']

Enter password length (minimum 8): 12

================================
Generated Password: G7mK2pQ9xR4a
================================

Generate another password? (Y/N): Y

Generated Password: aP8kL2xQ7mZ4

Generate another password? (Y/N): N

Thank you for using Password Generator!

The generated password will be different each time because the program uses random character selection.

```
### Program Logic


The program follows this workflow:

```
Start
  ↓
Select number of character types
  ↓
Validate number (2–4)
  ↓
Select U / L / N / S
  ↓
Validate selections
  ↓
Prevent duplicate selections
  ↓
Create combined character pool
  ↓
Enter password length
  ↓
Guarantee one character from each selected type
  ↓
Generate remaining random characters
  ↓
Shuffle password characters
  ↓
Display password
  ↓
Generate another?
  ↓
Yes → Generate again
No  → Exit
```


## 👨‍💻 Author

**Rupam Ghosh**

Electronics & Communication Engineering Graduate  
Aspiring Embedded Systems & Robotics Engineer

### 🔗 Connect With Me

- GitHub: [Rupam4604](https://github.com/Rupam4604)
- LinkedIn: [Rupam Ghosh](https://www.linkedin.com/in/rupam-ghosh-0406047119326s)