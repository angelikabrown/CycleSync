from flask import Flask 
from models import db, User
from os import path
from routes import init_routes
#from . import create_app



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyclesync.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'angie'  

    
    
   #initilaze the database with the app, connecting them
    db.init_app(app)

    #register the routes
    init_routes(app)

    #Create the database if it doesn't exist
    if not path.exists('cyclesync.db'):
        with app.app_context():
            db.create_all()
            print("Database created!")
            print(db)
            # existing_user = User.query.filter_by(username="joes").first()
            # if not existing_user:
            #     u2 = User(email="eat@joes", username="joes", password="password")
            #     db.session.add(u2)
            #     db.session.commit()
            # else:
            #     print("User with username 'joes' already exists.")
            #u5 = User(email="eat@jan", username="jan", password="passwurd")
            #db.session.add(u5)
            #db.session.commit()




    return app



# app.config['SITE_NAME'] = 'CycleSync'
# app.config['FLASK_DEBUG'] = 1


# with app.app_context():
#     db.create_all()
  
#     print("start")
#     print(db)

#      # Check if the username already exists
#     # existing_user = User.query.filter_by(username="joes").first()
#     # if not existing_user:
#     #     u2 = User(email="eat@joes", username="joes", password="password")
#     #     db.session.add(u2)
#     #     db.session.commit()
#     # else:
#     #     print("User with username 'joes' already exists.")
#     u4 = User(email="eat@bubba", username="bubba", password="password123")
#     db.session.add(u4)
#     db.session.commit()


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)



