import logging
from config import Config
from src.meeseek import Meeseek

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
config = Config()


if __name__ == "__main__":

    mrmeeseek = Meeseek(config=config, logger=logger)
    mrmeeseek.run()
