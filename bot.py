import os
import time
import threading
import praw
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Global counter for removals
removal_count = 0

def print_stats():
    """Periodically prints the total number of removed posts."""
    while True:
        time.sleep(3600)  # Log every 1 hour
        print(f"[STATS] Total scams removed so far: {removal_count}")

def run_bot():
    global removal_count
    
    # Start the stats thread
    stats_thread = threading.Thread(target=print_stats, daemon=True)
    stats_thread.start()

    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
        username=os.getenv("REDDIT_USERNAME"),
    )

    target_sub = os.getenv("TARGET_SUBREDDIT")
    scam_terms = ["cheapgpt.store", "95% off", "12$ only", "perplexity ai pro"]

    # Use try-except to handle connection errors or missing credentials
    try:
        me = reddit.user.me()
        print(f"Bot connected as {me}. Monitoring r/{target_sub}...")
    except Exception as e:
        print(f"Failed to connect to Reddit: {e}")
        return

    subreddit = reddit.subreddit(target_sub)
    
    # Stream for real-time removal
    for submission in subreddit.stream.submissions(skip_existing=True):
        content = (submission.title + submission.selftext).lower()
        
        if any(term in content for term in scam_terms):
            try:
                submission.mod.remove()
                removal_count += 1
                print(f"Removed: {submission.title}")
            except Exception as e:
                print(f"Failed to remove {submission.id}: {e}")

if __name__ == "__main__":
    run_bot()
