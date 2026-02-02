# Use a secure, slim Python image
FROM python:3.11-slim

# Set environment variables for security and performance
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user for security (HSE requirement)
RUN useradd -m hse_user
WORKDIR /app

# Install system dependencies for PDF processing
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Change ownership to the non-root user
RUN chown -R hse_user:hse_user /app
USER hse_user

# Expose the port (e.g., for a dashboard)
EXPOSE 8501

# Command to run the application
CMD ["python", "src/model.py"]