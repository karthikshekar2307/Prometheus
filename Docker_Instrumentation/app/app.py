from flask import Flask, request, Response
from prometheus_client import Counter, generate_latest

# Prometheus counter to count incoming requests
REQUEST_COUNT = Counter("app_request_counter", "Total Number of Requests made to the Application")

app = Flask(__name__)

@app.route("/")
def hello_team():
    REQUEST_COUNT.inc()  # Increment counter on each request
    return "Hello Team, This is from Docker WSGI....."

@app.route("/metrics")
def metrics():
    # Expose Prometheus metrics
    return Response(generate_latest(), status=200, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
