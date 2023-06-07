FROM python:3.6

WORKDIR /app

# Copy the load generation script
COPY loadgen.py .

# Install required packages
RUN pip install requests

# Set the command to run the load generation script
CMD [ "python", "loadgen.py" ]

