# threadbot
Thanks for new Telegram feature - comments, this bot generating someting like threads on reddit
-----------------
I didnt host this bot, but source code is open and you can do it if you want, so here is instruction:

First you should to do thats create channel and give there admin permissions for bot. Now bot can posting on your channel.

Than you should create discussion chat for using new feature.

-----------------
Also i put config.py in .gitignore so you should create it in root directory. 

File looks like:


BOT_TOKEN = 'Your token'

CHAT_ID = 'Your channel name' #it looks like @mychannel.


-----------------
Unfortunately telegram bot api does not allow creating channels automatically, so you have to do everything manually


Also I put readme in /help and commands description in /commands
-----------------
