from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Docker image built successfully using GitHub Actions."

@app.route("/about")
def about():
    return "This is a simple Flask application running inside Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
