from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .auth import login_handler, verify_handler

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        
        login_handler(email)
        
        return redirect(url_for('main.verify'))
    
    return render_template('login.html')


@main.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        otp_entered = request.form['otp']

        if verify_handler(otp_entered):
            return redirect(url_for('main.index'))
        else:
            flash("رمز اشتباه است. مجدد امتحان کنید.")

    return render_template('verify.html')