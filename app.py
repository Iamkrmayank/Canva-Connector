import os
from flask import Flask, jsonify

app = Flask(__name__)

festival_greetings = [
    {
        "id": "diwali_card_001",
        "fields": {
            "greeting_prefix": "Happy",
            "festival_name": "Diwali",
            "message": "Let’s celebrate the festival of lights with joy in our hearts and peace in our homes.",
            "footer": "@Suvichaar"
        }
    }
]

@app.route("/canva/data", methods=["GET"])
def get_festival_data():
    return jsonify({"items": festival_greetings})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # default to 5000 locally
    app.run(host="0.0.0.0", port=port)
