import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "stockapi"
NEWS_API = "newsapi"

#twilio 
account_sid = "accountsid"
auth_token = "authtoken"

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API,
}
response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])

#Getting the day before yesterday's closing stock price
before_yesterday_data = data_list[1]
before_yesterday_closing_price = float(before_yesterday_data['4. close'])


#Finding the positive difference 
difference = abs(yesterday_closing_price - before_yesterday_closing_price)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = difference / yesterday_closing_price

#percentage is greater than 5 then print("Get News").
if percent_diff > 0:
    news_params = {
        "apikey" : NEWS_API,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}, \nBrief: {article['description']}"for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
        body=article,
        from_='+13344384439',
        to='+917010799778',
        )
        print(message.status)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

