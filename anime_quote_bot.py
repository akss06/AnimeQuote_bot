import praw
import requests
import time
from dotenv import load_dotenv
import os
import anime_names
import random


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

subreddit = reddit.subreddit("testquo")

respond = set()

for comment in subreddit.stream.comments(skip_existing=True):
    
    
    found = False
    
    for aname in anime_names.anime_names:
        
        
        if aname.lower() in comment.body.lower() and key in comment.body.lower():
            found = True
            
            if comment.id not in respond:
                    
                    page = random.randint(0,11)
                    choice = random.randint(0,5)
                    
                    quotes = requests.get(f'https://animechan.vercel.app/api/quotes/anime?title={aname}&page={page}')
                    quote = quotes.json()[choice]['quote']
                    anime = aname.title()
                    
                    
                    character = quotes.json()[choice]['character']        

                    start = "**Anime Quote bot here!**\n\n"
                    main = "\n\t" + anime  + "\n\t" + f"\"{quote}\"" +  "\n\t" + f"-{character}"
                    end = "\n [Creator](https://www.reddit.com/user/rocknpaperss)"
                
                    comment.reply(start + main + end)
                    respond.add(comment.id)
                    time.sleep(15)
                    break
            
          
    
    if not found and key in comment.body.lower() and comment.id not in respond :
        quotes = requests.get("https://animechan.vercel.app/api/random")
        quote = quotes.json()['quote']
        character = quotes.json()['character']
        anime = quotes.json()['anime']
                       
        start = "**Anime Quote bot here!**\n\n"
        main = "\n\t" + anime  + "\n\t" + f"\"{quote}\"" +  "\n\t" + f"-{character}"
        end = "\n [Creator](https://www.reddit.com/user/rocknpaperss)"
                    
        comment.reply(start + main + end)
        respond.add(comment.id)
        time.sleep(15)

                
            
       
    
    
    
    
    
    
            
      
        
