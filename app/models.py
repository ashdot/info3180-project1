from app import db 


class Property(db.Model):

    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True) #property_id 

    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(255),nullable=False)
    
    number_of_bedrooms = db.Column(db.Integer,nullable=False)
    number_of_bathrooms = db.Column(db.Integer,nullable=False)


    location = db.Column(db.String(50),nullable=False)

    price = db.Column(db.Integer, nullable=False)

    property_type = db.Column(db.String(20),nullable=False)


    photo_filename = db.Column(db.String(255),nullable=False)

    #photo, title,description, no of bedrooms, no of bathrooms, location and price, house and apartment


    def __init__(self, title, description, number_of_bedrooms, number_of_bathrooms, location, price, property_type, photo_filename):

        self.title = title
        self.description = description
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.location = location
        self.price = price
        self.property_type = property_type
        self.photo_filename=photo_filename
