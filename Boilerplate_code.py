#Importing flask module in the project
from flask import Flask,render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

def first_flask():

    return "This is my first flask program"

@app.route("/second Page")
def second_flask():
    i = 'flask program'
    return render_template('index.html', image = i)

#run the application on local server
app.run()
