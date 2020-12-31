# Demo website
# Deploying on local host
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is home page."

@app.route('/about/')
def about():
    return "This is about page."

if __name__ == "__main__":
    app.run(debug=True)