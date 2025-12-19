# Reddit Scam Filter Bot

A fast, lightweight Reddit moderation bot built with Python and `praw`, managed by `uv`. Designed to monitor a specific subreddit and remove posts containing scam keywords.

## Features
- **Real-time Monitoring**: Uses Reddit's submission stream for instant action.
- **Scam Detection**: Automatically removes posts containing pre-defined scam terms.
- **Lightweight**: Uses `uv` for dependency management and a slim Docker image.
- **Easy Deployment**: Ready for TrueNAS or any Docker-compatible environment.

## Prerequisites
- [uv](https://github.com/astral-sh/uv) installed locally for development.
- Reddit API credentials (Client ID, Client Secret, Username, Password).

## Local Setup

1. **Clone the repository** (if applicable).
2. **Configure Environment Variables**:
   Copy the template `.env` and fill in your Reddit credentials:
   ```bash
   cp .env.template .env  # Or just edit the existing .env if already present
   ```
   Provide the following:
   - `REDDIT_CLIENT_ID`
   - `REDDIT_CLIENT_SECRET`
   - `REDDIT_USERNAME`
   - `REDDIT_PASSWORD`
   - `TARGET_SUBREDDIT` (e.g., `Comma_ai`)

3. **Install Dependencies & Run**:
   `uv` will automatically handle the environment and dependencies:
   ```bash
   uv run bot.py
   ```

## Docker Setup

### Build the Image
```bash
docker build -t reddit-bot .
```

### Run the Container
```bash
docker run -d \
  --name reddit-bot \
  --env-file .env \
  reddit-bot
```

## TrueNAS Deployment

1. Copy `bot.py`, `.env`, and `Dockerfile` to a directory on your TrueNAS pool.
2. In the TrueNAS **Apps** section, select **Launch Docker Image**.
3. Point to your `Dockerfile`.
4. **Crucial**: Bind mount the directory where your `.env` file lives or manually input the environment variables into the TrueNAS App configuration.

## Customizing Scam Terms
The scam terms are defined in `bot.py`:
```python
scam_terms = ["cheapgpt.store", "95% off", "12$ only", "perplexity ai pro"]
```
Modify this list to suit your needs.
