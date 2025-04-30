from flask import Flask, jsonify

app = Flask(__name__)

festival_greetings = [
    {
        "id": "diwali_card_001",  # Unique ID
        "fields": {
            "greeting_prefix": "Happy",
            "festival_name": "Diwali",
            "message": "Let’s celebrate the festival of lights with joy in our hearts and peace in our homes.",
            "footer": "@REALLYGREATSITE"
        }
    }
]

@app.route("/canva/data", methods=["GET"])
def get_festival_data():
    return jsonify({"items": festival_greetings})

if __name__ == "__main__":
    app.run(debug=True)
