import string

password = input("Enter your password: ")
score = 0

# Check password criteria
if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in string.punctuation for char in password):
    score += 1

# Display password strength
if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Moderate Password")
else:
    print("Strong Password")

# Recommendations
print("\nRecommendations to improve your password:")

if len(password) < 8:
    print("- Make your password at least 8 characters long.")

if not any(char.isupper() for char in password):
    print("- Add at least one uppercase letter (A-Z).")

if not any(char.islower() for char in password):
    print("- Add at least one lowercase letter (a-z).")

if not any(char.isdigit() for char in password):
    print("- Include at least one number (0-9).")

if not any(char in string.punctuation for char in password):
    print("- Include at least one special character (!, @, #, $, etc.).")

# If password is already strong
if (
    len(password) >= 8 and
    any(char.isupper() for char in password) and
    any(char.islower() for char in password) and
    any(char.isdigit() for char in password) and
    any(char in string.punctuation for char in password)
):
    print("Your password already follows all the recommended security practices!")
