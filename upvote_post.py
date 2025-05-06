import os
import praw
import random

# Environment variables for Reddit credentials
REDDIT_CLIENT_ID = os.environ["REDDIT_CLIENT_ID"]
REDDIT_CLIENT_SECRET = os.environ["REDDIT_CLIENT_SECRET"]
REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
REDDIT_PASSWORD = os.environ["REDDIT_PASSWORD"]
TARGET_SUBREDDIT = os.environ["TARGET_SUBREDDIT"]  # Subreddit to target

def main():
    # Authenticate with Reddit API
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent="daily-reddit-upvote-bot"
    )

    # Fetch the top 50 hot posts from the target subreddit
    subreddit = reddit.subreddit(TARGET_SUBREDDIT)
    posts = list(subreddit.hot(limit=50))

    # Choose a random post to upvote
    random_post = random.choice(posts)

    # Upvote the post and log the action
    random_post.upvote()
    print(f"Successfully upvoted: {random_post.title} (URL: {random_post.url})")

if __name__ == "__main__":
    main()
