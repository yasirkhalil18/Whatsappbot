# AiNotes WhatsApp Bot

This smart AI-powered WhatsApp bot helps students get free notes, books, and past papers via WhatsApp using Twilio + Flask + Render.

---

## 🧠 Features
- Understands English, Roman Urdu, and Hinglish
- Supports all boards: Punjab, FBISE, KPK, Sindh, AJK, etc.
- Matches subject, class, and board
- Replies with correct clickable note link from [https://ainotes.pk](https://ainotes.pk)

---

## 🚀 Deployment Steps

### 1. GitHub Setup
- Push this full project to a new GitHub repo

### 2. Render.com Deployment
- Create a new Web Service
- Connect your GitHub repo
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

### 3. Twilio Setup
- Go to Twilio > WhatsApp Sandbox
- Set Webhook URL: `https://your-render-url/whatsapp`

---

## ✅ Usage Example

**User Message:**
