from flask import Flask
from main import main


def create_app():
    app = Flask(__name__)  
    # app.config['SECRET_KEY'] = 'your_secret_key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['FLASK_ENV'] = 'development'
    # app.config['DEBUG'] = True


    app.register_blueprint(main)
    

    from main import db
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app
