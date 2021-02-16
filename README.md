# Mr. MeeSeeks Stockbot

I'm Mr. Meeseeks. I have to fulfill my purpose so I can go away. Look at me.

If using docker swarm deploy me like this:
```
env $(cat .env | xargs) docker stack deploy -c docker-compose.yaml stockbot
```
Don't forget to create your **.env** file

# Commands

```
/forex   Lookup for forex ticker. This are the options AUDUSD EURUSD EURGBP
         GBPJPY GBPUSD NZDUSD USDCAD USDCHF USDJPY BTCUSD

/crypto  Same as forex but here you can use * to lookup for options. 
         Eg.: btc* -> BTCUSDT BTCEUR and so on.

/company If you don't remember the ticker of the company. You can use this
         to get a hint.

/stock   Company's information

/news    Top 5 news from yahoo finance. You can use the ticker or the company's
         fullname.
         
/zacks   Zacks investment Rank and Score based on ticker
```

Feel free to help me build this funny bot.

Docker Hub: https://hub.docker.com/r/yvalencia/telegram-stockbot-mrmeeseek

Source: Finviz Yahoo Finance Binance