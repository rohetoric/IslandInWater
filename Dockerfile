# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy script to container
COPY island_in_water.py islands.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Set command to run script
CMD ["python3", "island_in_water.py", "islands.txt"]