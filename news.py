from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()
today = datetime.date.today().strftime("%Y-%m-%d")
yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")


class NewsFeed:
    base_url = 'https://newsapi.org/v2/top-headlines'
    API_KEY = os.getenv('API_KEY')

    def __init__(self, category, from_date=yesterday, to_date=today, language="en", number_of_articles=10):
        """
        possible catagory options: business, entertainment, general, health, science, sports, technology
        """
        self.category = category
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
        self.number_of_articles = number_of_articles

    def get(self):
        url = f'{self.base_url}?' \
              f'category={self.category}&' \
              'country=us&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              'sortBy=popularity&' \
              f'pageSize={self.number_of_articles}&' \
              f'apiKey={self.API_KEY}'
        res = requests.get(url)
        content = res.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + f"{article['title']}\n{article['url']}\n\n"

        return email_body


if __name__ == "__main__":
    print(yesterday)
    # news = NewsFeed(category="general")
    # print(news.get())
