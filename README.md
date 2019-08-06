# Pig Latin Bot

This is a simple GroupMe that will listen to group messages and put them into Pig Latin if a user starts their message with 'piglatinfy'.

### Steps To Run:
1. Get a GroupMe account and navigate to the [Developer Area](https://dev.groupme.com/bots)
2. Create a bot with the Callback URL pointing to the URL where this repo is hosted and where the server is running (the endpoint is `/groupme`; for example: `21.45.39.91/groupme`)
3. Download and install this repository, Python, and other dependencies where it can receive requests from the Callback URL in step 2
4. Copy the `Bot ID` from the GroupMe Developers page for step 5
5. Run this command: `BOT_ID={Bot ID from step 4} python3 app.py`
