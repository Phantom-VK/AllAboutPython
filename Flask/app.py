from flask import Flask, render_template,  request

'''
CREATES AN INSTANCE OF THE FLASK CLASS, WHICH WILL
BE OUR WSGI (Web Server Gateway Interface) application 
'''

# WSGI Application
app=Flask(__name__)


@app.route("/")
def index():
     return render_template('index.html')

@app.route(rule = "/form", methods = ['GET'])
def form():
     return render_template('form.html')

@app.route(rule = "/submit", methods = ['GET', 'POST'])
def submit():
     if request.method == 'POST':
          firstname = request.form["firstname"]
          return f"Hello {firstname}"
     return render_template('form.html')

if __name__ == "__main__":
     app.run(debug=True)