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
        url = f"https://finviz.com/api/quote.ashx?ticker={context.args[0].upper()}&instrument=forex&timeframe=d&type=new"
        result = requests.get(url, headers=headers).json()
        info_string = give_format_forex(**result)
    else:
        info_string = "Just one ticker at a time please."

    update.message.reply_text(info_string)


def crypto(update, context):
    if len(context.args) == 1:
        url = f"https://www.binance.com/exchange-api/v2/public/asset-service/product/get-products?includeEtf=false"
        result = requests.get(url, headers=headers).json()

        if "*" in context.args[0]:
            info_string = crypto_matches(currency=context.args[0].upper(), exchanges=result["data"])
        else:
            info_string = crypto_rate(currency=context.args[0].upper(), rates=result["data"])
    else:
        info_string = "Something went wrong. Try again."

    update.message.reply_text(info_string)


def news(update, context):
    if len(context.args) >= 1:
        query = "%20".join(context.args)
        url = f"https://query2.finance.yahoo.com/v1/finance/search?q={query.lower()}&lang=en-US&region=US&quotesCount=0&newsCount=5"
        result = requests.get(url, headers=headers).json()
        info_string = ""

        if len(result["news"]) > 0:
            for news in result["news"]:
                info_string += f"Title: {news['title']}\nPublisher: {news['publisher']}\nLink: {news['link']}\n" \
                               f"-----------------------\n "
        else:
            info_string = "I couldn't find any news. Sorry."

    else:

        info_string = "Something went wrong while looking for news. Try again."

    update.message.reply_text(info_string)


def zacks(update, context):
    if len(context.args) == 1:
        ticker = context.args[0].upper()
        url_rank = f"https://quote-feed.zacks.com/index.php?t={ticker}"
        url_score = f"https://www.zacks.com/stock/quote/{ticker}?q={ticker}"
        zacks_rank = requests.get(url_rank, headers=headers).json()
        raw_html = requests.get(url_score, headers=headers).text
        style_score = scrap_zacks_score(raw_html=raw_html)

        if len(zacks_rank) > 0 and len(style_score) > 0:
            info_string = f"Company Name: {zacks_rank[ticker]['name']}\nZacks Rank: {zacks_rank[ticker]['zacks_rank']} ({zacks_rank[ticker]['zacks_rank_text']})\nStyle Score: {style_score}"
        else:
            info_string = "I couldn't find any news. Sorry."

    else:

        info_string = "Just one ticker at a time."

    update.message.reply_text(info_string)
