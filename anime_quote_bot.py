import praw
import requests
import time
from dotenv import load_dotenv
import os


load_dotenv()


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
PASSWORD = os.getenv("PASSWORD")
USERNAME = os.getenv("USER")

reddit = praw.Reddit(
    client_id= CLIENT_ID,
    client_secret= CLIENT_SECRET,
    password= PASSWORD,
    user_agent="anime-quotes",
    username= USERNAME,
)

key = "!animequote"

subreddit = reddit.subreddit("IndianTeenagers")

respond = set()

for comment in subreddit.stream.comments(skip_existing=True):
    if key in comment.body.lower():
       if  comment.id not in respond:
        quotes = requests.get("https://kyoko.rei.my.id/api/quotes.php")
            
        quote = quotes.json()['apiResult'][0]['english']
        character = quotes.json()["apiResult"][0]['character']
        anime = quotes.json()["apiResult"][0]['anime']
            
        start = "**Anime Quote bot here!**\n\n"
        main = "\n\t" + anime  + "\n\t" + f"\"{quote}\"" +  "\n\t" + f"-{character}"
        end = "\n ######[Creator](https://www.reddit.com/user/rocknpaperss)"
        
        comment.reply(start + main + end)
        time.sleep(10)
        
    continue
    
    
    
    
    
    
            
      
        
