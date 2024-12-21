from flask import Flask, render_template, request
from chatbot_logic import create_chatbot

app = Flask(__name__)
chatbot = create_chatbot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg")
    response = chatbot.get_response(user_text)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
