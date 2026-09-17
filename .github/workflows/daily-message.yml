name: Telegram Bot Daily Notifier

on:
  schedule:
    - cron: '29 16 * * *'
  workflow_dispatch:

jobs:
  send-message:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install requests

      - name: Run bot script
        run: |
          python bot.py
        working-directory: .
