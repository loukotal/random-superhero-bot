from flask import Flask, request, Response
from bot.bot import heroes_names, mastodon_inst
import os

app = Flask(__name__)

auth_key = os.getenv("AUTH_KEY")

@app.route("/", methods=["GET"])
def index():
    # TODO: render html template with the basic information?
    return "SUP"


@app.route("/generate/", methods=["POST"])
def generate_one():
    # TODO: Add some sort of authorization for generating?
    if request.method == "POST":
        prediction = heroes_names.generate(n=1, return_as_list=True)

        return Response(prediction[0])

@app.route("/post/", methods=["POST"])
def post_toot():
    if request.method == "POST":
        data = request.get_json()

        auth = data.get("auth")

        if auth != auth_key:
            return Response(status=401)


        prediction = heroes_names.generate(n=1, return_as_list=True)
        mastodon_inst.status_post("New superhero on the block!\n\n{}".format(prediction))
        return Response(prediction[0])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
