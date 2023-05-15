FROM python:3.10-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

# Expose port 5000 for the Flask app
EXPOSE 5000

# Copy the current directory contents into the container at /app
COPY . /app

ENTRYPOINT ["flask", "run"]
