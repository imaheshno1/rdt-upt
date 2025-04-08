import praw
import os
import time
import random
import schedule
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('reddit_upvoter.log'), logging.StreamHandler()]
)
logger = logging.getLogger('reddit_upvoter')

# Load environment variables
load_dotenv()

def reddit_login():
    """Connect to Reddit API"""
    try:
        reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            username=os.getenv('REDDIT_USERNAME'),
            password=os.getenv('REDDIT_PASSWORD'),
            user_agent="script:RedditDailyUpvoter:v1.0 (by u/" + os.getenv('REDDIT_USERNAME') + ")"
        )
        logger.info(f"Logged in as: {reddit.user.me()}")
        return reddit
    except Exception as e:
        logger.error(f"Failed to log in: {e}")
        return None

def upvote_post(reddit):
    """Find and upvote a post from your chosen subreddit"""
    if not reddit:
        return
    
    try:
        # Configure this to your preferred subreddit
        subreddit_name = os.getenv('TARGET_SUBREDDIT', 'memes')
        subreddit = reddit.subreddit(subreddit_name)
        
        # Get hot posts from the subreddit
        posts = list(subreddit.hot(limit=20))
        
        # Choose a random post from the top posts
        if posts:
            post = random.choice(posts)
            
            # Upvote the post
            post.upvote()
            logger.info(f"Upvoted post: '{post.title}' in r/{subreddit_name}")
            
            # Optional: Add a short delay to avoid looking like a bot
            time.sleep(random.uniform(2, 5))
            return True
        else:
            logger.warning(f"No posts found in r/{subreddit_name}")
            return False
    except Exception as e:
        logger.error(f"Error upvoting post: {e}")
        return False

def daily_task():
    """Main function to run daily"""
    logger.info("Starting daily upvote task")
    reddit = reddit_login()
    success = upvote_post(reddit)
    logger.info(f"Daily task completed. Success: {success}")

def main():
    # Run once on startup
    daily_task()
    
    # Schedule to run daily at a specific time (adjust time as needed)
    schedule.every().day.at("10:30").do(daily_task)
    
    # Keep the script running
    logger.info("Script is running. Press Ctrl+C to exit.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        logger.info("Script stopped by user")

if __name__ == "__main__":
    main()
