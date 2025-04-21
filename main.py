class User:
    def __init__(self, id, email, username, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password


        # getter methods
    def get_email(self):
        return self.email


    def get_username(self):
        return self.username


    def get_password(self):
        return self.password



class Data:
    def __init__(self, temperature, mood, energy, notes, date, timestamp):
        self.temperature = temperature
        self.mood = mood
        self.energy = energy
        self.notes = notes
        self.date = date
        self.timestamp = timestamp




