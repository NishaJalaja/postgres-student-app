# Use a slim version of Python to keep the AWS Fargate image small
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Set environment variables to ensure Python output is sent to logs immediately
ENV PYTHONUNBUFFERED=1

# Copy only requirements first to optimize Docker's build cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your service's code
COPY . .

# The command to run your service (update main.py to your entry file)
CMD ["python", "main.py"]
