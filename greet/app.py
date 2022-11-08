from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_greet():
    return 'Welcome!'

@app.route('/welcome/home')
def home_greet():
    return 'Welcome home!'

@app.route('/welcome/back')
def back_greet():
    return 'Welcome back!'