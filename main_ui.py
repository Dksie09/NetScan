from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='color:purple'>HELLO WORLD</h1>"

@app.route("/about")
def about():
    return "<h1 style='color:yellow'>yay</h1>"

if __name__ == "__main__":
    app.run(debug=True)