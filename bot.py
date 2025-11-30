import os
import requests
import schedule
import time
from dotenv import load_dotenv
from telegram import Bot

# ----------------------------
# 1. Load environment variables
# ----------------------------
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

# ----------------------------------------------------
# 2. Fetch a random motivational quote from an API
# ----------------------------------------------------
def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        data = response.json()[0]

        quote = data.get("q", "Believe in yourself.")
        author = data.get("a", "Unknown")

        return f"💡 *Daily Motivation*\n\n{quote}\n\n— _{author}_"
    except Exception as e:
        print("API error:", e)
        return "💪 Stay strong! Even small steps move you forward."

# ----------------------------------------------------
# 3. Send message to Telegram
# ----------------------------------------------------
def send_quote():
    try:
        message = get_quote()
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")
        print("Quote sent successfully.")
    except Exception as e:
        print("Error sending message:", e)

# ----------------------------------------------------
# 4. Schedule the bot to run daily at 8:00 AM
# ----------------------------------------------------
schedule.every().day.at("08:00").do(send_quote)

print("Daily Motivation Bot is running...")

# ----------------------------------------------------
# 5. Keep the bot alive
# ----------------------------------------------------
while True:
    schedule.run_pending()
    time.sleep(1)
