# Password Strength Checker

A simple Python application that evaluates the strength of a user's password based on common cybersecurity best practices. The program analyzes the password against multiple security criteria, assigns a strength score, classifies the password as **Weak**, **Moderate**, or **Strong**, and provides recommendations for improving password security.

---

## Features

- Checks if the password is at least **8 characters** long.
- Verifies the presence of:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Special characters (!, @, #, $, %, etc.)
- Calculates a password strength score.
- Classifies passwords into:
  - Weak
  - Moderate
  - Strong
- Provides personalized recommendations for creating a more secure password.

---

## Technologies Used

- Python 3
- `string` module
- Built-in Python functions:
  - `any()`
  - `isupper()`
  - `islower()`
  - `isdigit()`

---


##  Password Evaluation Criteria

| Security Requirement | Score |
|----------------------|:-----:|
| Minimum length (8 characters) | ✅ |
| Uppercase letter | ✅ |
| Lowercase letter | ✅ |
| Number | ✅ |
| Special character | ✅ |

Maximum Score: **5**

### Classification

| Score | Password Strength |
|:-----:|-------------------|
| 0–2 | Weak |
| 3–4 | Moderate |
| 5 | Strong |

---

## Learning Objectives

This project was built to strengthen my understanding of:

- Python fundamentals
- Conditional statements
- Loops and generators
- String manipulation
- Built-in functions
- Basic cybersecurity concepts
- Password validation techniques

---

## Future Improvements

- Prevent common dictionary passwords.
- Detect repeated or sequential characters.
- Estimate password entropy.
- Add a graphical user interface (GUI) using Tkinter.
- Build a web version using Flask or Django.

---

## Author

**Khadija Ashraf**

Computer Systems Engineering Student 
