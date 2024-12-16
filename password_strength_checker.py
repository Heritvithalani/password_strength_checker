import re

# Constants
MIN_LENGTH = 8
MAX_LENGTH = 12
SPECIAL_CHARS = "!@#$%^&*()-_+=<>?/|"

def check_password_strength(password):
    score = 0

    # Penalize for common weak patterns
    if re.search(r"(1234|password|qwerty)", password.lower()):
        return -2

    # Check Length
    if MIN_LENGTH <= len(password) <= MAX_LENGTH:
        score += 2
    elif len(password) > MAX_LENGTH:
        score += 1  # Bonus for extra length

    # Check for uppercase
    if any(char.isupper() for char in password):
        score += 1

    # Check for lowercase
    if any(char.islower() for char in password):
        score += 1

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1

    # Check for special characters
    if any(char in SPECIAL_CHARS for char in password):
        score += 1

    return score

def password_feedback(score):
    if score <= 3:
        return "Weak: Consider making it longer with mixed characters."
    elif 4 <= score <= 6:  # Adjusted range for "Moderate"
        return "Moderate: Add more variety for better security."
    else:  # Scores ≥ 7
        return "Strong: Your password looks good!"

if __name__ == "__main__":
    password = input("Enter your password: ")
    score = check_password_strength(password)
    feedback = password_feedback(score)
    print(f"Password Strength: {feedback}") 