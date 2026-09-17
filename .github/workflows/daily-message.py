name: Telegram Bot Daily Notifier

on:
  schedule:
    # 21:50 Toshkent vaqti (UTC+5) = 16:50 UTC
    - cron: "56 16 * * *"
  workflow_dispatch: {}

jobs:
  send-message:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install requests

      - name: Run bot script
        env:
          BOT_TOKEN: ${{ secrets.8997993468:AAGt8nAcu0TZCuLe8qBEiIgZpeTA9y2qXoE}}
          CHAT_ID: ${{ secrets.-1003811990608}}
        run: python bot.py
