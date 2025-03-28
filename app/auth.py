from flask import session
import random

otp_store = {}

def login_handler(email):
    otp = str(random.randint(100000, 999999))
    otp_store[email] = otp # todo: Use redis
    
    print(otp)
    # todo: Send OTP via email
    session['pending_email'] = email
    return
        
def verify_handler(otp):

    email = session.get('pending_email')

    if email and otp_store.get(email) == otp:
        session['user_email'] = email
        del otp_store[email]
        return True
    else:
        return False

    