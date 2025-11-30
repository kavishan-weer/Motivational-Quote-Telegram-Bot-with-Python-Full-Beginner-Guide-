Daily Motivation Bot

A simple Python project that sends a motivational quote every day using a reliable quotes API.
This bot is lightweight, easy to modify, and perfect for beginners learning Python, APIs, and automation.

📌 About This Project

Originally this bot used another quotes API that became unstable and caused SSL errors.
Because of that, this version now uses the more stable and reliable ZenQuotes API, which works consistently.

This repo contains the updated and fixed version.


✨ Features

Fetches a new motivational quote every day

Uses a stable API (ZenQuotes)

Clean & simple Python code

Can be extended for:

Telegram bots

Discord bots

Email notifications

Cron/scheduled jobs


📂 Project Structure
daily_motivation_bot/

│── bot.py

│── requirements.txt

│── README.md


🔧 Installation
1. Clone the repository
git clone https://github.com/yourusername/daily_motivation_bot.git

cd daily_motivation_bot


2. Install dependencies
pip install -r requirements.txt

▶️ How to Run
python3 bot.py


You will see a new motivational quote printed in the terminal.


🧠 How It Works

Makes a request to the ZenQuotes API

Receives a JSON response

Extracts the quote and author

Prints it cleanly


📝 Example Output
"Your only limit is your mind."
— Anonymous
