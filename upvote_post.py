import os
import praw
import random

REDDIT_CLIENT_ID = os.environ["REDDIT_CLIENT_ID"]
REDDIT_CLIENT_SECRET = os.environ["REDDIT_CLIENT_SECRET"]
REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
REDDIT_PASSWORD = os.environ["REDDIT_PASSWORD"]
TARGET_SUBREDDIT = os.environ["TARGET_SUBREDDIT"]  # The subreddit to target

def main():
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent="github-reddit-upvote-bot"  # Hardcoded user agent
    )

    # Fetch posts from the target subreddit
    subreddit = reddit.subreddit(TARGET_SUBREDDIT)
    posts = list(subreddit.hot(limit=50))  # Fetch the top 50 hot posts

    # Choose a random post from the list
    random_post = random.choice(posts)

    # Upvote the selected post
    random_post.upvote()
    print(f"Upvoted: {random_post.title} (URL: {random_post.url})")

if __name__ == "__main__":
    main()
