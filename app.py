from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App updated  Running Inside Docker!"

@app.route("/about")
def about():
    return "Learning DevOps Step by Step"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
