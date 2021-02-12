import finviz
import requests

from src.utils import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36'
}


def stock(update, context):
    info_string = ""

    if len(context.args) == 1:

        ticker_info = finviz.get_stock(context.args[0])
        keys = ["Company", "Sector", "Industry", "Market Cap", "Price", "P/E", "52W Range", "Earnings", "Perf YTD",
                "Change", "Dividend", "Dividend %"]

        for ticker in ticker_info:
            if ticker in keys:
                info_string = info_string + f"{ticker}: {ticker_info[ticker]}\n"

    else:
        info_string = "I can handle just one ticker at the time."

    update.message.reply_text(info_string)


def company(update, context):

    if len(context.args) == 1:
        url = f"https://finviz.com/api/suggestions.ashx?input={context.args[0]}"
        result = requests.get(url, headers=headers).json()
        info_string = evaluate_coincidences(result)
    else:
        info_string = "Yo! Remember just one word!"

    update.message.reply_text(info_string)


def forex(update, context):

    if len(context.args) == 1:
        url = f"https://finviz.com/api/quote.ashx?ticker={context.args[0].upper()}&instrument=forex&timeframe=i5&type=new"
        result = requests.get(url, headers=headers).json()
        info_string = give_format_forex(**result)
    else:
        info_string = "Just one ticker at a time please."

    update.message.reply_text(info_string)
