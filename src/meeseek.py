import sys
from telegram.ext import Updater, CommandHandler
from src.actions import *


class Meeseek:

    def __init__(self, config, logger):
        self.updater = Updater(config.TOKEN, use_context=True)
        self.config = config
        self.logger = logger

        self.dp = self.updater.dispatcher
        self.dp.add_handler(CommandHandler("stock", stock, pass_args=True))
        self.dp.add_handler(CommandHandler("company", company, pass_args=True))
        self.dp.add_handler(CommandHandler("forex", forex, pass_args=True))
        self.dp.add_error_handler(self.error)

    def run(self):
        """
        Depending if its DEV or PRO this function will start a polling or a webhook
        """
        if self.config.MODE == "DEV":
            self.updater.start_polling()
            self.updater.idle()
        elif self.config.MODE == "PRO":
            self.updater.start_webhook(listen="0.0.0.0", port=self.config.PORT, url_path=self.config.TOKEN)
            self.updater.bot.set_webhook(f"https://{self.config.HEROKU_APP_NAME}.herokuapp.com/{self.config.TOKEN}")
        else:
            self.logger.info("MODE is not specify. Try DEV or PRO.")
            sys.exit()

    def error(self, update, context):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)
        update.message.reply_text("I'm sorry something went wrong. I couldn't find that ticker in finviz.")
