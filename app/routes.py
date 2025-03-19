from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone', '')  # Optional field
    address = request.form.get('address', '')  # Optional field

    if phone and (not phone.isdigit() or len(phone) != 10):
        return "Phone number must be exactly 10 digits!", 400

    user = User(name=name, email=email, phone=phone, address=address)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))