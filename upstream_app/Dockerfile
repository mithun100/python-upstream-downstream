FROM python:3.6

WORKDIR /app

# Install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port on which the application will run (optional)
EXPOSE 5000

# Set the command to run the application
CMD [ "python", "upstream_app.py" ]
