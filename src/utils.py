import fnmatch


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
            Something went wrong with your ticker. Remember I only know:\n
            AUDUSD\n
            EURUSD\n
            EURGBP\n
            GBPJPY\n
            GBPUSD\n
            NZDUSD\n
            USDCAD\n
            USDCHF\n
            USDJPY\n
            BTCUSD\n
            """
    else:
        return f"Data 24h timeframe\n\nExchange: {kwargs['name']}\nLast Open: {kwargs['lastOpen']}\nLast Close: {kwargs['lastClose']}\nHigh:{kwargs['lastHigh']}\nLow: {kwargs['lastLow']}"


def crypto_rate(currency, rates):
    for exchange in rates:
        if exchange["s"] == currency:
            return f"Exchange: {currency}\nPrice: {float(exchange['c'])}"

    return "I couldn't find this exchange."


def crypto_matches(currency, exchanges):
    matches = [exchange['s'] for exchange in exchanges if fnmatch.fnmatch(exchange["s"], currency.upper())]
    return "\n".join(matches)
