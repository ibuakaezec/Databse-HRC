from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template ("index.html")

@app.route('/home')
def home():
    return render_template ("home.html")

@app.route('/other')
def other():
    return render_template ("other.html")

@app.route('/reports')
def reports():
    return render_template ("reports.html")

@app.route('/survey')
def survey():
    return render_template ("survey.html")


if __name__ == "__main__":
    app.run()
