from flask import Flask, request, jsonify
import logging
import json
import datetime
import settings
from main_bot import bot
from telebot import types


logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

app = Flask(__name__)
secret = "7707284304"


@app.route(f"/bot/{secret}/", methods=["POST"])
def webhook():
    if request.method == "POST":
        text = request.get_data().decode("utf-8")
        logging.info("Request: %s", text)
        request_body_dict = json.loads(text)
        update = types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
    return {"statusCode": 200}


@app.route("/")
def hello_world():
    return "Hello from Flask!"


if __name__ == "__main__":
    app.run(debug=True)
