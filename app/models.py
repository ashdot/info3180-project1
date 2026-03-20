from . import db 


class Property(db.Model):

    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)


    def __init__(self):

       pass

