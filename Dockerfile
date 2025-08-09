# Start from the official Prefect image as base
FROM prefecthq/prefect:3-latest

# Set working directory in container
WORKDIR /app

# Copy requirements file first (for better Docker layer caching)
COPY requirements.txt .

# Install custom Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code (flows, scripts, etc.)
COPY . .

# Expose port 4200 for Prefect server
EXPOSE 4200

# Default command (will be overridden by docker-compose)
CMD ["prefect", "server", "start", "--host", "0.0.0.0"]