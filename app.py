from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from googlesearch import search

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ WhatsApp Bot is Running — Ask for class/subject/board notes."

@app.route("/webhook", methods=["POST"])
def webhook():
    user_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    query = f"{user_msg} site:ainotes.pk"
    print(f"🔍 Searching for: {query}")

    try:
        results = list(search(query, num_results=1))
        if results:
            link = results[0]
            msg.body(f"🔗 Here's the best match I found:\n👉 {link}")
        else:
            msg.body("❌ Sorry! No result found. Please try again with class, subject, and board.")
    except Exception as e:
        msg.body("⚠️ Bot error. Please try again later.")
        print("Error:", e)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
