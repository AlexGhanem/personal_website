from flask import Flask, render_template, redirect
from datetime import datetime
from connection import cursor
# Configure application
app = Flask(__name__)

cursor.execute('SELECT * FROM PROJECTS')
results = cursor.fetchall()


@app.route('/', methods=['GET', 'POST']) 
def home():
    greeting = "Welcome to Alex's Portfolio"
    return render_template('home.html', greeting=greeting, projects=results)


@app.route('/projects')
def projects():
    return render_template('projects.html', projects=results)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/fires')
def fires_page():
    return render_template('fires.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
