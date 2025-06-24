from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from message_handler import generate_reply

app = Flask(__name__)

@app.route("/whatsapp", methods=["GET", "POST"])
def whatsapp():
    if request.method == "GET":
        return "👋 Yeh AiNotes WhatsApp bot ka webhook hai. Sirf POST request Twilio ke liye allow hai."

    msg = request.form.get("Body", "")
    resp = MessagingResponse()
    resp.message(generate_reply(msg))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
