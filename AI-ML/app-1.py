#msg="welcome to my youtube channel"
#print(msg)
from flask import Flask
app =Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my youtube channel'


if __name__=='__main__':
    app.run()


# building uri dynamically
# variable rules and url building

from flask import Flask
### WSGI Application
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to My Youtube Channel. Please Please subscribe my channel"


@app.route('/members')
def members():
    return "Welcome to My Youtube Channel members"



if __name__=='__main__':
    app.run(debug=True)


