# Telegram Bot for Transaction Status

## Overview

This Telegram bot is designed to receive UUIDs (Universally Unique Identifiers) from users, check the status of transactions associated with these UUIDs, and provide responses accordingly. It can be used in various scenarios where transaction tracking or verification is required.

## Features

- Accepts UUIDs from users through Telegram messages.
- Provides real-time responses to users with transaction status information.

## Usage

To use this Telegram bot, follow these steps:

1. Start a conversation with the bot on Telegram.

2. Send your UUID to the bot.

3. The bot will process the UUID and check the transaction status.

4. You will receive a response with the status of your transaction.

## Installation and Configuration
This project serves as an example for running the `bot.py` application. To successfully run the application, you will need a Python virtual environment and the installation of required packages from `requirements.txt`.

- Clone the repository: 
```
git clone git@github.com:funnydevelopment/RoundbizStatus.git
```
and navigate to the project folder.

- Create a Python virtual environment: 
```
python -m venv venv
```

- Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```

On macOS and Linux:
```
source venv/bin/activate
```

- Install the necessary dependencies from requirements.txt: 
```
pip install -r requirements.txt
```
- Run the project:
```
python bot.py
```