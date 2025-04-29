import os
import praw

REDDIT_CLIENT_ID = os.environ["REDDIT_CLIENT_ID"]
REDDIT_CLIENT_SECRET = os.environ["REDDIT_CLIENT_SECRET"]
REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
REDDIT_PASSWORD = os.environ["REDDIT_PASSWORD"]
REDDIT_POST_URL = os.environ["REDDIT_POST_URL"]

def main():
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent="github-reddit-upvote-bot"  # Hardcoded user agent
    )
    submission = reddit.submission(url=REDDIT_POST_URL)
    submission.upvote()
    print(f"Upvoted: {REDDIT_POST_URL}")

if __name__ == "__main__":
    main()
