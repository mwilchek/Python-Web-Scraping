import praw
from datetime import datetime
from collections import namedtuple
import pandas as pd

# set PRAW API reqs
reddit = praw.Reddit(client_id='nyk9gIgRru0IMQ',
                     client_secret='****************',
                     user_agent='windows:com.praw.testapp:v1 (by /u/SkyNet_Developer)')

# Create submission tuple object with features
Submission = namedtuple('Submission', ['Date', 'Poster_Name', 'Post_Title', 'Link', 'Content'])

# Create list to append data to
data = []

# Declare subreddit to scrape
subreddit = reddit.subreddit('BaltimoreAndDCr4r')

# Loop through subreddit's submissions collecting features and appending to list
for submission in subreddit.new(limit=5000):
    if "F4M" in submission.title:
        time = submission.created
        date = datetime.fromtimestamp(time)

        author = submission.author
        title = submission.title
        link = submission.url
        text = submission.selftext

        data.append(Submission(date, author, title, link, text))

# Create dataframe from list of data
df = pd.DataFrame(data)

# Declare filename for output
filename = 'reddit_data.csv'

# Output dataframe to csv file
df.to_csv(filename, index=False, encoding='utf-8')
