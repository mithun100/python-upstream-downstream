from flask import Flask, request
import requests

app = Flask(__name__)

# Downstream application URL
downstream_url = "http://python-downstream-service"

@app.route("/", methods=["GET"])
def root():
    # Make a request to the downstream application
    downstream_response = requests.get(downstream_url)
    
    # Return the downstream response as the response from the upstream application
    #return downstream_response.content, downstream_response.status_code, downstream_response.headers
    if downstream_response.status_code == 200:
        return downstream_response.text

# Regular route for other URLs
@app.route("/other", methods=["GET"])
def other():
    return "This is a regular route in the upstream application."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
