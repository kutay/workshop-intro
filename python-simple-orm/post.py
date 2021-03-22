from orm import Model

class Post(Model):

    text = str  # other datatypes: int, float

    def __init__(self, text):
        self.text = text