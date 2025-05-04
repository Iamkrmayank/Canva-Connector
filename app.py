from flask import Flask, jsonify, request, redirect
import os
import requests
import base64
import hashlib
import secrets

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

# In-memory storage for PKCE (for demo/testing only; use secure DB or session in production)
PKCE_STORE = {}

CANVA_CLIENT_ID = os.getenv("CANVA_CLIENT_ID")
CANVA_CLIENT_SECRET = os.getenv("CANVA_CLIENT_SECRET")
REDIRECT_URI = "https://web-production-9738.up.railway.app/oauth/redirect"

# ========== 📤 Live App Data ==========
@app.route("/canva/data", methods=["GET"])
def get_festival_data():
    return jsonify({"items": festival_greetings})

# ========== 🔐 Step 1: Start OAuth with PKCE ==========
@app.route("/canva/auth", methods=["GET"])
def start_auth():
    code_verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b"=").decode("utf-8")
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).rstrip(b"=").decode("utf-8")

    # Save the code_verifier (in-memory for this session)
    PKCE_STORE["verifier"] = code_verifier

    auth_url = (
        "https://www.canva.com/api/oauth/authorize"
        f"?response_type=code"
        f"&client_id={CANVA_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=design:content:read design:meta:read design:content:write asset:read asset:write brandtemplate:content:read profile:read"
        f"&code_challenge_method=S256"
        f"&code_challenge={code_challenge}"
    )
    return redirect(auth_url)

# ========== 🔐 Step 2: Handle Redirect from Canva ==========
@app.route("/oauth/redirect")
def oauth_redirect():
    code = request.args.get("code")
    if not code:
        return "❌ Missing authorization code", 400

    code_verifier = PKCE_STORE.get("verifier")
    if not code_verifier:
        return "❌ Code verifier missing from store", 400

    token_url = "https://api.canva.com/api/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": CANVA_CLIENT_ID,
        "client_secret": CANVA_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code_verifier": code_verifier
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        return "✅ OAuth flow completed successfully. You can now submit to Canva."
    else:
        return f"❌ OAuth failed. Response: {response.text}", 500

# ========== 🔁 Return Navigation ==========
@app.route("/return-nav")
def return_nav():
    return "✅ Return navigation successful. You may close this tab."

# ========== 🚀 Main ==========
if __name__ == "__main__":
    app.run(debug=True)
