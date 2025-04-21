from flask import render_template, session
from CycleSync.models import User, Data
#from flask_login import LoginManager, UserMixin

from . import create_app
app = create_app()

#login_manager = LoginManager(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.config['SITE_NAME'] = 'CycleSync'
app.config['FLASK_DEBUG'] = 1

if __name__ == "__main__":
    app.run(debug=True)