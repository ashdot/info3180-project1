"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app,db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from .forms import PropertyForm
from .models import Property
from werkzeug.utils import secure_filename
import os 


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties', methods=['GET'])
def properties():
    """Shows Properties"""

    all_properties = db.session.execute(
        db.select(Property).order_by(Property.id)
    ).scalars().all()

    return render_template("properties.html", properties=all_properties)

@app.route('/properties/create', methods=['GET','POST'])
def new_properties():
    """Creates Properties"""

    form = PropertyForm()

    if form.validate_on_submit():



        #photo, title,description, no of bedrooms, no of bathrooms, location and price, house and apartment

        photo = form.photo.data

        title = form.title.data 
        description = form.description.data
        no_of_bedrooms = form.number_of_bedrooms.data
        no_of_bathrooms = form.number_of_bathrooms.data
        location = form.location.data
        price = form.price.data

        property_type = form.property_type.data

        filename = secure_filename(photo.filename)
        photo_path = os.path.join(app.root_path, 'static', 'uploads', filename)
        photo.save(photo_path)

        new_property = Property (

            title = title, 
            description=description,
            number_of_bedrooms=no_of_bedrooms,
            number_of_bathrooms=no_of_bathrooms,
            location=location, 
            price = price, 
            property_type=property_type,
            photo_filename=filename  
        )


        db.session.add(new_property)
        db.session.commit()



        
        flash('Property Added', 'success')
        return redirect(url_for('properties'))


  
    return render_template('newproperty.html', form=form)


@app.route('/properties/<property_id>', methods=['GET'])
def get_properties(property_id):
    """Gets a single Property"""

    property = db.session.get(Property, property_id)

    return render_template('property.html', property=property)

@app.route('/uploads/<filename>')
def get_property_photo(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)




###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
