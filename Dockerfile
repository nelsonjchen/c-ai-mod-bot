# Use a slim Python image
FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy pyproject.toml
COPY pyproject.toml .

# Install dependencies using uv
# --system tells uv to install into the image's python env directly
RUN uv pip install --system -r pyproject.toml

# Copy the bot script
COPY bot.py .

# Run the bot
CMD ["python", "bot.py"]
