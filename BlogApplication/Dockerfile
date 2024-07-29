FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Create logs directory
RUN mkdir -p /app/logs

# Make sure the script is executable
RUN chmod +x /app/django.sh

EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["/app/django.sh"]
