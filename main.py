import praw   # pip install praw
import pandas as pd
import json
import urllib
import time

clientId = ""
clientSecret = ""
userAgent = ""
userName = ""
userPassword = ""

# Reddit Creds are stored in a json file and is put in .gitignore for safekeeping
# To read the data fro a Json file
file = open("data.json")
data = json.load(file)
for i,j in  data["reddit_creds"].items():   # The .items() is mandatory to unpack values form the dictionary
    if i == "client_id":
        clientId = j
    elif i == "client_secret":
        clientSecret = j
    elif i == "user_agent":
        userAgent = j
    elif i == "userName":
        userPassword = j


# In the reddit website, go to user settings => security & privacy => authorize 3rd party apps and
# enter the details. client id and client secret will be generated.
reddit = praw.Reddit(
    client_id = clientId,
    client_secret = clientSecret,
    user_agent = userAgent,
    # username = userName,
    # password = userPassword
)

subreddit = reddit.subreddit("aww")
# To get the comments for a post, use the post's url
submission = reddit.submission(url="https://www.reddit.com/r/Python/comments/t2cnr5/what_python_automation_have_you_created_that_you/")

dictionary = {
    "Title": [],
    "Post Text": [], 
    "Score": [],
    "Total Comments": [], 
    "Post URL": []
}

for post in subreddit.new(limit=5):
    dictionary["Title"].append(post.title)
    dictionary["Post Text"].append(post.selftext)
    dictionary["Score"].append(post.score)
    dictionary["Total Comments"].append(post.num_comments)
    dictionary["Post URL"].append(post.url)

# pandas is used to make a 2d table using the data extracted
# top_posts = pd.DataFrame(dictionary)
# top_posts

# for top_level_comment in submission.comments:
#     print(top_level_comment.body)

# Downloading image locally
count = 0
for  submissions in subreddit.new(limit=10):
    if "jpg" in submissions.url.lower() or "png" in submissions.url.lower():
        url = submissions.url
        print(url)
        urllib.request.urlretrieve(url, f"C:/Users/iloke/Downloads/reddit_img-{str(count)}.jpg")
        time.sleep(5)
        count += 1
        print(count)