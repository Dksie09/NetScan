from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/get_ip", methods=["POST"])
def get_ip():
    ip = request.form.get('ip-address')
    return "Your IP is: " + ip


if __name__ == "__main__":
    app.run(debug=True)