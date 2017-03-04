__author__ = 'Martin Fiser'
__credits__ = 'Martin Fiser, 2017, Twitter: @VFisa'

# Import Libraries
import os
from config import *
import praw
import pprint
import time

# Environment setup
abspath = os.path.abspath(__file__)
script_path = os.path.dirname(abspath)
os.chdir(script_path)
print script_path


def output_file(output, name):
    """
    Save output data as txt file
    """
    timestamp = (time.strftime("%Y-%m-%d %H-%M-%S"))
    filename = (str(timestamp)+" - "+str(name))

    text_file = open(filename, "w")
    text_file.write(str(output))
    text_file.close()



reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)


print(reddit.read_only)

"""
for submission in reddit.subreddit('learnpython').hot(limit=100):
    print(submission.title)
"""

#subreddit = reddit.subreddit('/r/vancouver')
subreddit = reddit.subreddit('vancouver/new')

print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
print(subreddit.description)   # Output: A subreddit for discussion of 

submission = reddit.submission(url='https://www.reddit.com/r/vancouver/comments/5xgzb3/fyi_ubc_bus_loop_changes_as_of_march_6th/')

top_level_comments = list(submission.comments)
all_comments = submission.comments.list()

output_file(all_comments, "all_comments")


