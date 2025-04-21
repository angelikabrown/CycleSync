from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager(app)
import PassionProject.CycleSync.main as main


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.config['SITE_NAME'] = 'CycleSync'
app.config['FLASK_DEBUG'] = 1

if __name__ == "__main__":
    app.run(debug=True)