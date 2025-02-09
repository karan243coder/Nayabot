# Use the official Python image from the Docker Hub as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container's working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port (optional, but useful if you are hosting a web server, e.g., Flask)
EXPOSE 8080

# Command to run the bot (or start your Flask app if using Flask)
CMD ["python", "bot.py"]
