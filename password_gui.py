import tkinter as tk
from password_strength_checker import check_password_strength, password_feedback

# Function to evaluate password strength and update the result label
def evaluate_password():
    password = password_entry.get()
    score = check_password_strength(password)
    feedback = password_feedback(score)
    
    # Update result label text and color based on feedback
    result_label.config(text=feedback)
    if score <= 3:
        result_label.config(fg="red")
    elif score <= 5:
        result_label.config(fg="orange")
    else:
        result_label.config(fg="green")

# Create the main application window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")  # Set window size

# Add a label for instructions
instruction_label = tk.Label(root, text="Enter your password below to check its strength:", font=("Arial", 12))
instruction_label.pack(pady=10)

# Add an entry widget for password input
password_entry = tk.Entry(root, show="*", width=30, font=("Arial", 14))
password_entry.pack(pady=10)

# Add a button to trigger password evaluation
check_button = tk.Button(root, text="Check Password", command=evaluate_password, font=("Arial", 12), bg="blue", fg="white")
check_button.pack(pady=10)

# Add a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
