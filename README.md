Daily Motivation Bot

A simple Python script that sends you a fresh motivational quote every day using the ZenQuotes API.
This project is perfect for learning basic Python scripting, APIs, and automation.

🚀 Features

Fetches a new motivational quote every time it runs

Uses a stable API (alternative to unreliable ones)

Lightweight and beginner-friendly

Customizable for:

Telegram bots

Discord bots

Email senders

Mobile notifications

Cron jobs / scheduled tasks

📁 Project Structure
daily_motivation_bot/
│── bot.py
│── README.md
│── requirements.txt

🛠️ Installation
1. Clone the repository
git clone https://github.com/kavishan-weer/Motivational-Quote-Telegram-Bot-with-Python-Full-Beginner-Guide-
cd daily_motivation_bot

2. Install dependencies
pip install -r requirements.txt

📜 Usage

Simply run:

python3 bot.py


You will see a motivational quote printed in your terminal.

🧩 How It Works

The script sends a request to the ZenQuotes API

Receives a JSON response

Extracts the quote + author

Prints it nicely formatted

🧪 Sample Output
"Your only limit is your mind."
— Anonymous
