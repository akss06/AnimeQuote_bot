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

subreddit = reddit.subreddit("testquo")

respond = set()

for comment in subreddit.stream.comments(skip_existing=True):
    
    if "!animequote random" in comment.body.lower() and comment.id not in respond :
        quotes = requests.get("https://animechan.vercel.app/api/random")
        quote = quotes.json()['quote']
        character = quotes.json()['character']
        anime = quotes.json()['anime']
                       
        start = "**Anime Quote bot here!**\n\n"
        main = main = "\n\t" + anime  + "\n\t" + f"\"{quote}\"" +  "\n\t" + f"-{character}"
        end = "\n [Creator](https://www.reddit.com/user/rocknpaperss)"
                    
        comment.reply(start + main + end)
        respond.add(comment.id)
        time.sleep(15)
         
    
    found = False
    
    for aname in anime_names.anime_names:
        
        
        if aname.lower() in comment.body.lower() and "!animequote" in comment.body.lower():
            found = True
            
            if comment.id not in respond:
                    
                    page = random.randint(0,11)
                    
                    
                    quotes = requests.get(f'https://animechan.vercel.app/api/quotes/anime?title={aname}&page={page}')
                    
                    if type(quotes.json()) == list:
                        quote = quotes.json()[random.randint(0, len(quotes.json())-1)]['quote']
                        anime = aname.title()
                        character = quotes.json()[random.randint(0, len(quotes.json())-1)]['character']        

                    else:
                        try:
                            quote = quotes.json()['quote']
                            anime = aname.title()
                            character = quotes.json()['character']   

                        except KeyError:
                            
                            start = "**Anime Quote bot here!**\n\n"
                            main = "\n\tSorry, no quotes found :("
                            end = "\n [Creator](https://www.reddit.com/user/rocknpaperss)"     
                            comment.reply(start + main + end)
                            respond.add(comment.id)
                            time.sleep(15)
                            continue
                    
                    start = "**Anime Quote bot here!**\n\n"
                    main = "\n\t" + anime  + "\n\t" + f"\"{quote}\"" +  "\n\t" + f"-{character}"
                    end = "\n [Creator](https://www.reddit.com/user/rocknpaperss)"
                    
                    comment.reply(start + main + end)
                    respond.add(comment.id)
                    time.sleep(15)
                    break
    
    
    
    if not found and '!animequote' in comment.body.lower() and comment.id not in respond :
        
        start = "**Anime Quote bot here!**\n\n"
        main = "\n\tSorry, the requested anime is not available :("
        end = "\n [Creator](https://www.reddit.com/user/rocknpaperss)"
                    
        comment.reply(start + main + end)
        respond.add(comment.id)
        time.sleep(15)

                
            
       
    
    
    
    
    
    
            
      
        
