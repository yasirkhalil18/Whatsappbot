import os
from flask import Flask, request
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
from message_handler import generate_reply

# Load from .env
load_dotenv()
DEBUG_MODE = os.getenv("DEBUG", "False") == "True"

app = Flask(__name__)

@app.route("/whatsapp", methods=["GET", "POST"])
def whatsapp():
    if request.method == "GET":
        return "👋 Yeh AiNotes WhatsApp bot ka webhook hai. Sirf POST request Twilio ke liye hoti hai."
    
    msg = request.form.get("Body", "")
    resp = MessagingResponse()
    resp.message(generate_reply(msg))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)
