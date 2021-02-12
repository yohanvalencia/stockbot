def evaluate_coincidences(coincidences):
    def unpacking_results(ticker, company, exchange):

        table = f"""Ticker: {ticker}\nCompany: {company}\nExchange: {exchange}"""

        return table

    if len(coincidences) == 0:
        return "I couldn't find any coincidence. Try another word."
    else:
        table = f"Hey! I found {len(coincidences)} coincidences. Check them out:\n\n"
        for result in coincidences:
            table += unpacking_results(**result) + "\n------------------------------\n"
        return table


def give_format_forex(**kwargs):
    if len(kwargs) <= 2:
        return \
            """
            Something went wrong with your ticker. Remember I only know:\
            AUDUSD\
            EURUSD\
            EURGBP\
            GBPJPY\
            GBPUSD\
            NZDUSD\
            USDCAD\
            USDCHF\
            USDJPY\
            BTCUSD\
            """
    else:
        return f"Data in 5 minutes timeframe\n\nForex: {kwargs['name']}\nCurrent: {kwargs['lastClose']}\nHigh:{kwargs['lastHigh']}\nLow: {kwargs['lastLow']}"
