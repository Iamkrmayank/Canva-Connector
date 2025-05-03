from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

# ========== 🎉 Greeting Card Data ==========
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

# ========== 📤 Live App Data Endpoint ==========
@app.route("/canva/data", methods=["GET"])
def get_festival_data():
    return jsonify({"items": festival_greetings})


# ========== 🔐 OAuth Redirect ==========
@app.route("/oauth/redirect")
def oauth_redirect():
    code = request.args.get("code")
    if not code:
        return "Missing authorization code", 400

    token_url = "https://api.canva.com/auth/token"
    client_id = os.getenv("CANVA_CLIENT_ID")
    client_secret = os.getenv("CANVA_CLIENT_SECRET")
    redirect_uri = "https://canva-connector-production.up.railway.app/oauth/redirect"

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        return "✅ OAuth flow completed successfully. You can now submit to Canva."
    else:
        return f"❌ OAuth failed. Response: {response.text}", 500


# ========== 🔁 Return Navigation (Optional) ==========
@app.route("/return-nav")
def return_nav():
    return "✅ Return navigation successful. You may close this tab."


# ========== 🚀 Main ==========
if __name__ == "__main__":
    app.run(debug=True)
