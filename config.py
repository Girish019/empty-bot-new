# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Bot Information
API_ID = int(environ.get("API_ID", "10755921"))
API_HASH = environ.get("API_HASH", "d5e49fd3637cba407f17807d31c77977")
BOT_TOKEN = environ.get("BOT_TOKEN","1677559691:AAFSzVlg46NhmtNOYdMU08NVuWy6s0KBbYM")  # zee5cc
# BOT_TOKEN = environ.get("BOT_TOKEN",  "6137898485:AAEzJaeA-K784RS-xN3Q_EzcL_uXA1WkxQA")  # lmc


PICS = (environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')).split() # Bot Start Picture
OWNER_ID = environ.get("OWNER_ID", "")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "PROFStrail_bot") # without @
PORT = environ.get("PORT", "8080")
# ADMINS.append(OWNER_ID)
ADMINS.append(1147676731)
ADMINS.append(1284476297)
ADMINS.append(5636224141)

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', True)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://Tessa:tessa33@practice1.3mqtowb.mongodb.net/?retryWrites=true&w=majority")
CDB_NAME = environ.get("CDB_NAME", "NC_CLONE_FS")

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://Tessa:tessa33@practice1.3mqtowb.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "NC_filestore")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
FILE_STORE_CHANNEL = int(environ.get("FILE_STORE_CHANNEL", "-1001842556179"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001748750847"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', False)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "api.shareus.io") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "hRPS5vvZc0OGOEUQJMJzPiojoVK2") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/How_To_Open_Linkl") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', False)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "https://filestorebotsdemo.blogspot.com/2024/08/dot-serials.html") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")

PYTHON_VERSION = environ.get("PYTHON_VERSION", "3.10.8")
# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
    
