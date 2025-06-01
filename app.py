from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/login")
def login():
    return "login"



@app.route("/register")
def register():
    return "login"


if __name__ == '__main__':
    app.run()
