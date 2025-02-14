# building uri dynamically
# variable rules and url building

from flask import Flask,redirect,url_for,render_template
### WSGI Application
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to My Youtube Channel. Please Please subscribe my channel"


@app.route('/members')
def members():
    return "Welcome to My Youtube Channel members"

@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the marks is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

###Result checker
@app.route('/results/<int:marks>')
def result(marks):
     result=""
     if marks<50: 
        result='fail'
     else:
        result='success'
     return redirect(url_for(result,score=marks))         


if __name__=='__main__':
    app.run(debug=True)