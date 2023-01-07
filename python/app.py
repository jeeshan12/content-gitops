from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Setting up Github actions for fluxCD"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
