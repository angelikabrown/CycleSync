from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager(app)
import main


# app.config['SECRET_KEY'] = 'your_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)