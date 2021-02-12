from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    TOKEN = os.getenv("TOKEN")
    MODE = os.getenv("MODE").upper()
    HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME").lower()
    PORT = int(os.getenv("PORT"))
