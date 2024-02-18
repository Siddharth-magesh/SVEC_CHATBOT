from flask import Flask, render_template, request
from main_chat_bot import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", text=None)

@app.route("/chatbot", methods=["POST"])
def get_number():
    user_input = request.form["chatname"].lower()  # Convert input to lowercase for case-insensitive matching
    result=main_function(user_input)
    return render_template("index.html", text=result)

if __name__ == "__main__":
    app.run(debug=True)