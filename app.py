from flask import Flask, jsonify

app = Flask(__name__)

festival_greetings = [
    {
        "id": "diwali_card_001",
        "fields": {
            "greeting_prefix": "Happy",
            "festival_name": "Diwali",
            "message": "Let’s celebrate the festival of lights with joy in our hearts and peace in our homes.",
            "footer": "@REALLYGREATSITE"
        }
    },
    {
        "id": "holi_card_001",
        "fields": {
            "greeting_prefix": "Happy",
            "festival_name": "Holi",
            "message": "Splash colors of joy and love this Holi!",
            "footer": "@ColorfulGreetings"
        }
    },
    {
        "id": "eid_card_001",
        "fields": {
            "greeting_prefix": "Eid Mubarak",
            "festival_name": "Eid",
            "message": "May this Eid bring peace, prosperity, and joy to your life.",
            "footer": "@PeaceAndBlessings"
        }
    },
    {
        "id": "christmas_card_001",
        "fields": {
            "greeting_prefix": "Merry",
            "festival_name": "Christmas",
            "message": "Wishing you a season filled with warmth, joy, and peace.",
            "footer": "@SantaSaysHi"
        }
    },
    {
        "id": "newyear_card_001",
        "fields": {
            "greeting_prefix": "Happy",
            "festival_name": "New Year",
            "message": "Cheers to a fresh start and new opportunities!",
            "footer": "@NewBeginnings"
        }
    }
]

@app.route("/canva/data", methods=["GET"])
def get_festival_data():
    return jsonify({"items": festival_greetings})

if __name__ == "__main__":
    app.run(debug=True)
