from flask import Flask
from routes import rt



def create_app():
    app = Flask(__name__)  
    # app.config['SECRET_KEY'] = 'your_secret_key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyclesync.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['FLASK_ENV'] = 'development'
    # app.config['DEBUG'] = True


    app.register_blueprint(rt)
    app.add_url_rule('/', endpoint='index')

    from main import db
   
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app
