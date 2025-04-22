from flask import render_template, session
from CycleSync.models import User, Data, db
#from flask_login import LoginManager, UserMixin

from . import create_app
app = create_app()

#login_manager = LoginManager(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.config['SITE_NAME'] = 'CycleSync'
app.config['FLASK_DEBUG'] = 1


with app.app_context():
    db.create_all()
  
    print("start")
    print(db)

     # Check if the username already exists
    # existing_user = User.query.filter_by(username="joes").first()
    # if not existing_user:
    #     u2 = User(email="eat@joes", username="joes", password="password")
    #     db.session.add(u2)
    #     db.session.commit()
    # else:
    #     print("User with username 'joes' already exists.")
    u4 = User(email="eat@bubba", username="bubba", password="password123")
    db.session.add(u4)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)



