from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, InputRequired


class PropertyForm(FlaskForm):
    title = StringField('Title',validators=[InputRequired()])

    number_of_bedrooms = StringField('Number of Bedrooms', validators=[InputRequired()])
    number_of_bathrooms = StringField('Number of Bathrooms', validators=[InputRequired()])

    location = StringField('Location', validators=[InputRequired()])

    price = StringField('Price', validators=[InputRequired()])

    type = SelectField('Type', choices=[])


    description = TextAreaField('Description', validators=[InputRequired()])


    photo = FileField('File', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
   