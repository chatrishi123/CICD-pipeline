import os
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)


APP_VERSION = os.environ.get("APP_VERSION", "dev")


@app.route("/")
def index():
    return jsonify(message="Hello from the CI/CD pipeline! (v2)", version=APP_VERSION)


@app.route("/health")
def health():
    # Used by load balancers / Docker health checks / Postman tests.
    return jsonify(status="ok", time=datetime.now(timezone.utc).isoformat())


@app.route("/api/echo/<text>")
def echo(text):
    return jsonify(echo=text, length=len(text))


if __name__ == "__main__":
    # Local development only. In the container, gunicorn runs the app.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
