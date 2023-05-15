#Step1: Import flask
from flask import Flask, render_template, request
import re

#Step2: Create object with parameter __name__
app = Flask(__name__)


#Step3: Creating end points and binding them with a functionality
################################################
# Route 1
@app.route('/')
def home_fun():
    return render_template('home.html')

# Route 2
@app.route('/regex', methods=['POST'])
def regex_fun():
    main_text = request.form.get('main_text')
    reg_text=request.form.get('test_text')
    match=re.findall(reg_text, main_text)
    total_matches=len(match)
    return render_template('result.html', match=match, total_matches=total_matches, main_text=main_text, reg_text=reg_text)


###############################################

if __name__ == '__main__':
    app.run(debug=True)