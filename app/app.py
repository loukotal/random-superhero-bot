from flask import Flask, request

from src.bot.bot import heroes_names

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # TODO: render html template with the basic information?
    return "SUP"


@app.route("/generate/", methods=["POST"])
def generate_one():
    # TODO: Add some sort of authorization for generating?
    if request.method == "POST":
        print(heroes_names.generate())
        print("WTF")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
