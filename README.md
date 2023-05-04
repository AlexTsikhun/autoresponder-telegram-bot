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
|
├───main.py                    <- Bot
|
└───requirements.txt           <- The requirements file for reproducing the analysis environment, e.g. generated with `pip freeze > requirements.txt`
```

### Solution
Telegram-bot, that you can chat with - this function provides OpenAI API (CHATGPT). Written in python, library aiogram. Bot, which contain information about users in database SQLite (telegram_db). 

Admin can send messages to 1000 users with command:

```
/send2all YOUR_MESSAGE
```

Program wrap in docker container for deploing. 

### An example of a completed task:
![image](https://user-images.githubusercontent.com/83775762/236190791-cf246a27-0463-4567-b74c-0f57bbf5064a.png)

List of users (0 - is not active user):
![image](https://user-images.githubusercontent.com/83775762/236192600-8ddaccd4-a34d-40ff-b9f1-241fbf97085c.png)

Bot can answer in Ukrainian:
![image](https://user-images.githubusercontent.com/83775762/236193101-ed00f0d8-11ee-4701-9eb7-60a0b6ac3b13.png)

