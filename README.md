# autoresponder-telegram-bot

## Development of an answering machine for telegrams
Task from: Royal Techno

General description of the task:

Development of a neural network language bot of telegrams
Language: Python
1. Sending messages by user base
2. Mailing to 1000 users in one session
DO NOT SPAM
3. "autoresponder" function

### Project Structure:
```
├───README.md                  <- The top-level README for developers using this project
|
├───.gitignore                 <- Ignore files
|
├───Dockerfile                 <- Assemble an image
|                             
├───docker-compose.yml         <- Defining services
|
├───telegram_db                <- SQLite database
|
├───db.py                      <- Database queries
├───main.py                    <- Bot
|
|
└───requirements.txt           <- The requirements file for reproducing the analysis environment, e.g. generated with `pip freeze > requirements.txt`
```

### Solution
Telegram-bot, that you can chat with - this function provides OpenAI API (CHATGPT). Writtern in python library aiogram Bot, which contain information about users in database SQLite (telegram_db). 

Admin can send messages to 1000 users with command:

```
/send2all YOUR_MESSAGE
```

Program wrap in docker container for deploing. 

