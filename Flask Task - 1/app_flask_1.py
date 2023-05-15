#App to create a backend server using python.
#The server url should take query parameters as a string and return it in upper case format


#Step 1: Import Flask and request
from flask import Flask, request

#Step 2: Create an object with parameter __name__
app=Flask(__name__)

user_name=['Anna','Bella','Jerry','Tom','Olive']
#Step 3: Creating end points and binding them with functions
@app.route('/')
def home_page():
    return "Welcome...!!"

@app.route('/add')
def add_page():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)+ int(b))

@app.route('/uppercase')
def upper_case():
    a=request.args.get('a')
    upper=a.upper()
    return upper

@app.route('/lowercase')
def lower_case():
    a=request.args.get('a')
    lower=a.lower()
    return lower

@app.route('/in/<user>')
def profile_page(user):
    if user in user_name:
        return f"Welcome {user}..!! =)"
    else:
        return "User name not found!"

#Step 4: Run the app
if __name__ == '__main__':
    app.run(debug=True)
