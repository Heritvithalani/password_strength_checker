from flask import Flask, request, render_template
from password_strength_checker import check_password_strength, password_feedback

# Initialize the Flask app
app = Flask(__name__)

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    feedback = ""  # Default feedback is empty
    if request.method == "POST":
        # Get the password from the form
        password = request.form["password"]
        
        # Process the password
        score = check_password_strength(password)
        feedback = password_feedback(score)
        
        # Debug print to ensure feedback is correct
        print(f"Password: {password}, Score: {score}, Feedback: {feedback}")
    
    # Render the HTML template and pass the feedback
    return render_template("index.html", feedback=feedback)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
