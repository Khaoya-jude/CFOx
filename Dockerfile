# ------------------------------
# Dockerfile for CFOx MCP App
# ------------------------------

# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app app
COPY scripts scripts

# Expose MCP port
ENV MCP_PORT=8000
EXPOSE 8000

# Start the app using FastMCP server entry
CMD ["python", "-m", "app.main"]