import requests
import time

upstream_url = "http://python-upstream-service:80"

# Continuously send GET requests to the Upstream endpoint
while True:
    response = requests.get(upstream_url)
    print("Response:", response.status_code)
    time.sleep(10)  # Adjust the delay between requests as needed

