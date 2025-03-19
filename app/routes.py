import re
from flask import render_template, request, redirect, url_for, flash
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

    # Server-side validation for email
    email_pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    if not re.match(email_pattern, email):
        flash("Please enter a valid email address (e.g., user@example.com)!")
        return redirect(url_for('index'))

    # Server-side validation for phone (if provided)
    if phone and (not phone.isdigit() or len(phone) != 10):
        flash("Phone number must be exactly 10 digits!")
        return redirect(url_for('index'))

    user = User(name=name, email=email, phone=phone, address=address)
    db.session.add(user)
    db.session.commit()
    flash("Data submitted successfully!", "success")
    return redirect(url_for('index'))