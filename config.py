import os

# Config file with secrets.
# DO NOT PUSH SECRETS TO GIT!

# PostgreSQL
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_hostname = os.environ['DB_HOSTNAME']
db_port = 6432
db_name = os.environ['DB_NAME']

# Telegram bot
bot_token = os.environ['BOT_TOKEN']

# Sentry
sentry_url = os.environ['SENTRY_URL']

# Other
thank_you_message = os.environ['THANK_YOU_MESSAGE']
