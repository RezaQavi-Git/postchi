from flask import Blueprint, render_template, request, session, redirect, url_for, flash
import random

main = Blueprint('main', __name__)

otp_store = {}

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        otp = str(random.randint(100000, 999999))
        otp_store[email] = otp # todo: use redis
        
        # todo: Send OTP via email
        
        session['pending_email'] = email
        return redirect(url_for('main.verify'))
    
    return render_template('login.html')


@main.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        email = session.get('pending_email')
        otp_entered = request.form['otp']

        if email and otp_store.get(email) == otp_entered:
            session['user_email'] = email
            del otp_store[email]
            return redirect(url_for('main.index'))
        else:
            flash("رمز اشتباه است. مجدد امتحان کنید.")

    return render_template('verify.html')