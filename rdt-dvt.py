import praw
import os
import random
import time

def downvote_post():
    """Find and downvote a post from a chosen subreddit"""
    try:
        # Get credentials from environment variables
        client_id = os.environ.get("REDDIT_CLIENT_ID")
        client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
        username = os.environ.get("REDDIT_USERNAME")
        password = os.environ.get("REDDIT_PASSWORD")
        subreddit_name = os.environ.get("TARGET_SUBREDDIT", "memes")
        
        # Initialize Reddit API
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent=f"script:RedditDailyDownvoter:v1.0 (by u/{username})"
        )
        
        # Verify login
        print(f"Logged in as: {reddit.user.me()}")
        
        # Get posts from subreddit
        subreddit = reddit.subreddit(subreddit_name)
        posts = list(subreddit.hot(limit=20))
        
        if not posts:
            print(f"No posts found in r/{subreddit_name}")
            return False
            
        # Choose random post and downvote
        post = random.choice(posts)
        post.downvote()
        print(f"Downvoted post: '{post.title}' in r/{subreddit_name}")
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    downvote_post()
