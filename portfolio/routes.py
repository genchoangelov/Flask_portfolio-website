import os

from portfolio import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

picFolder = os.path.join('portfolio', 'images')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/portfolio')
def my_portfolio_page():
    picTableau = os.path.join(app.config['UPLOAD_FOLDER'], 'tableau.jpg')
    return render_template('portfolio.html', user_image=picTableau)

@app.route('/resume')
def my_resume_page():
    return render_template('resume.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')