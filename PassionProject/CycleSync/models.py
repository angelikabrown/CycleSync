from flask_sqlalchemy import SQLAlchemy

#initialize the database extention
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    # Define the relationship with the Data model  
    #data = db.relationship('Data', backref='user', nullable=True)    

    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email }

    # def __init__(self, email, username, password):
    #     self.email = email
    #     self.username = username
    #     self.password = password


    #     # getter methods
    # def get_email(self):
    #     return self.email


    # def get_username(self):
    #     return self.username


    # def get_password(self):
    #     return self.password



class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    mood = db.Column(db.String(50))
    energy = db.Column(db.String(50))
    notes = db.Column(db.String(200))
    date = db.Column(db.String(50))
    timestamp = db.Column(db.String(50))
    # Define the relationship with the User model
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # Define the relationship with the Data model

    def __init__(self, temperature, mood, energy, notes, date, timestamp):
        self.temperature = temperature
        self.mood = mood
        self.energy = energy
        self.notes = notes
        self.date = date
        self.timestamp = timestamp

        # getter methods
    def get_temperature(self):
        return self.temperature
    
    def get_mood(self):
        return self.mood
    
    def get_energy(self):
        return self.energy
    
    def get_notes(self):
        return self.notes
    
    def get_date(self):
        return self.date




