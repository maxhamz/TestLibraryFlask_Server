# users/utils.py
import os
import secrets
import random
from PIL import Image
from flask import url_for, current_app, jsonify
from flask_mail import Message
from src import mail, bcrypt
from random import randint
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, decode_token
)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/propics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# def hash_passsword(rawPassword):
#     return bcrypt.generate_password_hash(rawPassword, rounds=10).decode("utf-8")

# def check_hash(stored, entered):
#     return bcrypt.check_password_hash(stored, entered)

# better use this instead!
def generateOTP():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0,9))
    
    return otp



def send_reset_email(user):

    """
        token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
    """

    print("SENDING RESET PASSWORD INSTRUCTION THRU EMAIL \n\n")
    print("DON'T FORGET THE OTP AS WELL! \n\n")
    otp = generateOTP()
    print(otp)
    payload = {
        'username': user['username'],
        'email': user['email'],
        'userid': user['id'],
        'propic': user['image_file'],
        'OTP': otp
    }

    

    print("THIS IS USER:")
    print(payload)

    access_token = create_access_token(identity=payload)

    print("THIS IS TOKEN\n\n")
    print(access_token)

    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user['email']])

    print("ACHTUNG! THIS IS MESSAGE!\n")
    # print(msg)
    # print("this is message body\n")
    # print(msg.body)

    msg.body = f'''To reset your password, enter the following OTP on reset pasword form:
    {otp}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    print("UPDATED MESSAGE SI: \n\n")
    print(msg)
    mail.send(msg)

    return payload


