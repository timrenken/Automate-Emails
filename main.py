from dotenv import load_dotenv
import pandas as pd
import os
import yagmail
from news import NewsFeed

load_dotenv()

df = pd.read_csv('people.csv')

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

email = yagmail.SMTP(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)

for index, row in df.iterrows():
    news_feed = NewsFeed(category=row['category'],
                         number_of_articles=row['number_of_articles'])
    email.send(to=row['email'],
               subject=f"{row['category'].title()} News for Today",
               contents=f"Greetings {row['first_name']}!\n\n"
                        f"Here the Top {row['number_of_articles']} news stories of the day!\n\n"
                        f"{news_feed.get()}"
                        "Best Regards,\n"
                        "Tim Renken")
