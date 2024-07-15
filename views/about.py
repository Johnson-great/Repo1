from flask import render_template, Blueprint

abouts = Blueprint('about', __name__)

@abouts.get('/about')
def about():
    return render_template('about.html')
