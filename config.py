import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env.dev')
load_dotenv(dotenv_path)

DATABASE_URL = os.environ.get('JA_DATABASE_URL')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
