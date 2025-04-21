from flask import Flask
from CycleSync.routes import rt



def create_app():
    app = Flask(__name__)  
    #is this where the database gets connected?
    # or should I make a config.py 
    app.config.from_object('config.Config')

    #register the blueprint that was defined in routes.py
    app.register_blueprint(rt)


    from CycleSync.models import db
   
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app
