import praw

import pyttsx3 as ptts
from video import *
import re

from passw import *


#default_subs = ["AmITheAsshole",'EntitledParents',"TIFU",'ProRevenge']
default_subs = ["ProRevenge"]
    
#class that extracts the reddit posts using the praw api
class Reddit:
    def __init__(self,subs=default_subs, numPosts = 5):
        self.reddit = praw.Reddit(
            client_id= client_id,
            client_secret =client_secret,
            password=password,
            user_agent=user_agent,
            username=username
        )
        self.subs = subs
        self.numPosts = numPosts
        self.topPosts = None

    def getSubs(self):
        return self.subs

    def getTopPosts(self, inclUpdates = False):
        if not self.topPosts:
            d = {}

            #grabs top posts for the week from specified subs
            for s in self.subs:
                posts = list(self.reddit.subreddit(s).top("week", limit=self.numPosts))
                if not inclUpdates:
                    for post in posts:
                        if "UPDATE" in post.title:
                            posts.remove(post)
                d[s] = posts
            self.topPosts = d

        return self.topPosts

    #grabs top controversial posts for the week from specified subs    
    def getControversialPosts(self):
        d = {}
        for s in self.subs:
            d[s] = self.reddit.subreddit(s).controversial("week", limit=self.numPosts)
        return d

f=open("posts.txt",'w')

red=Reddit(numPosts=2)     
tp=red.getTopPosts()
print('got top posts')

#writes posts into text file
for sub in tp:
    print(sub)
    for post in tp[sub]:
        f.write(post.title+"\n")
        f.write(post.selftext+'\n')


f.close()        

#replaces reddit new lines with normal new lines and removes any URL's, then rewrites the file
f= open("posts.txt",'r+')
testts= f.read().replace("&#x200B;", "\n")
testts = re.sub(r'http\S+','',testts)
f= open('posts.txt', 'w')
f.write(testts)
f.close()




videoGen = vid(210)

videoGen.makeClips()
videoGen.group()


