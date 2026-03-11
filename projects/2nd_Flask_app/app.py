from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! This app is running inside a Docker container."

@app.route("/health")
def health_check():
    return "Healthy", 200

@app.route("/info")
def info():
    return "This is a Flask app running inside a Docker container."




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)



#http://127.0.0.1:5001

#http://127.0.0.1:5001






