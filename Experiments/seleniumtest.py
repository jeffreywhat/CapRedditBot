#Need GoLogin Page
#Find driver path unconditionally
#Scraper 1.0 by /u/python_engineer

import pandas as pd
import praw
import gologin
from selenium import webdriver
from selenium.webdriver import Chrome
driver = webdriver.Chrome('path to driver')

#user_agent = ""

#reddit = praw.Reddit (
#client_id = "",
#client_secret = "",
#user_agent = user_agent
#)

headlines = set()
for submission in reddit.subreddit('Nvidia').hot(limit=None):
    headlines.add(submission.title)
print(len(headlines))


print(submission.title)
print(submission.id)
print(submission.author)
print(submission.score)
print(submission.upvote_ratio) #i.e. controversiality
print(submission.url) #not needed

df = pd.DataFrame(headlines)

# Set up a GoLogin profile
gologin.set_profile(
name="my-profile",
browser_executable_path="path to chrome.exe",
user_agent="my-user-agent",
proxy={
"server": "my-proxy-server",
"port": 1234, #port from goLogin
"username": "my-username",
"password": "my-password"
}
)

#driver = gologin.get_webdriver("my-profile", Chrome)

reddit = praw.Reddit(
#client_id="****",
#client_secret="****",
#user_agent="",
#webdriver=driver
)


driver.quit()