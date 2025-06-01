"""
Flask Web Application - Student Result Management System

This application demonstrates:
- Basic routing
- Form handling
- Template rendering
- Dynamic URL building
- Request methods (GET/POST)
- Error handling
- Template inheritance
- Static files
- Message flashing
- Session management
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session and flash messages

# Database simulation (in-memory for demonstration)
students_db = {
    'john@example.com': {
        'firstname': 'John',
        'lastname': 'Doe',
        'password': 'password123',
        'scores': {'math': 85, 'science': 72}
    }
}


@app.route("/")
def index():
    """Homepage route displaying welcome message"""
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
     Handle user login
     - GET: Show login form
     - POST: Process login credentials
     """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate credentials
        if email in students_db and students_db[email]['password'] == password:
            session['user'] = email  # Store user in session
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html')


@app.route("/dashboard")
def dashboard():
    """Display user dashboard after successful login"""
    if 'user' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('login'))

    user_email = session['user']
    student = students_db[user_email]
    return render_template('dashboard.html', student=student)


@app.route("/logout")
def logout():
    """Handle user logout by clearing session"""
    session.pop('user', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))


@app.route("/result/<subject>/<int:score>")
def show_result(subject, score):
    """
     Display result with dynamic parameters
     - subject: Subject name from URL
     - score: Numeric score from URL
     """
    result = "Pass" if score >= 40 else "Fail"

    # Additional feedback based on score ranges
    feedback = ""
    if score >= 80:
        feedback = "Excellent!"
    elif score >= 60:
        feedback = "Good job"
    elif score >= 40:
        feedback = "You passed"
    else:
        feedback = "Needs improvement"

    return render_template('result.html',
                           subject=subject,
                           score=score,
                           result=result,
                           feedback=feedback)


@app.route("/api/result/<int:score>")
def api_result(score):
    """
     API endpoint that returns JSON response
     Demonstrates RESTful API concept
     """
    result = "Pass" if score >= 40 else "Fail"
    return {
        "status": "success",
        "score": score,
        "result": result,
        "message": "Result retrieved successfully"
    }


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 error handler"""
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)