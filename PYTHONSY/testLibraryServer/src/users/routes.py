# users/routes.py
import json
# import jwt
from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify, abort
from flask_login import login_user, current_user, logout_user, login_required
from src import db, bcrypt
from src.models import User, Book
# from src.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
#                                    RequestResetForm, ResetPasswordForm)
from src.users.utils import save_picture, send_reset_email
# from flask_serialize import FlaskSerializeMixin
from src.config import Config
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, decode_token
)
# from errors.handlers import error_400, error_401, error_500


SECRETKEY = Config.SECRET_KEY

users = Blueprint("users", __name__)

# DECLARE NECESSARY GLOBALS
response = {
    'status': 200,
    'message': 'OK',
    'result': []
}

@staticmethod
@users.route("/users/register", methods=['POST'])
def register():
    print("REGSITER NEW USER")
    print(request.form, "\n\n")
    username = request.form.get('username')
    email = request.form.get('email')
    passwordRaw = request.form.get('password')

    rawUser = {
        'username': username,
        'email': email,
        'password': passwordRaw
    }

    print("what's email?")
    print(email, "\n")

    userExist = User.query.filter_by(email=email).first()

    if (userExist is not None):
        abort(400)
    else:
        user = User(rawUser)
        user.save()

        newUser = User.query.filter_by(email=email).first()
        newUser1 = newUser.as_dict()

        response['status'] = 201
        response['message'] = 'REGISTER SUCCESS'
        response['result'] = newUser1

        return jsonify(response)


@staticmethod
@users.route("/users/getall", methods=['GET'])
def getAll():
    print("GETTING ALL USER @ USER ROUTES")
    listUsers = User.get_all()

    newUserList = []

    # SERIALIZE EACH OBJECT INSIDE A LIST
    for user in listUsers:
        userJSON = user.as_dict()
        newUserList.append(userJSON)
    
    # print("HELLO LADIES! LET'S SEE USERS' LIST \n\n")
    # print(newUserList)

    response['status'] = 200
    response['message'] = 'FETCH ALL SUCCESS'
    response['result'] = newUserList

    return jsonify(response)



@staticmethod
@users.route("/users/getByUsername/<string:username>", methods=['GET'])
def getOneByUsername(username):
    user = User.query.filter_by(username=username).first_or_404()

    # print("GETTING ONE USERNAME BY USERNAME \n")
    # print(user)

    userJSON = user.as_dict()

    response['status'] = 200
    response['message'] = 'SUCCESS: GET BY USERNAME'
    response['result'] = userJSON

    return jsonify(response)



@staticmethod
@users.route("/users/getById/<string:userid>", methods=['GET'])
def getOneById(userid):
    user = User.query.filter_by(id=userid).first_or_404()

    # print("GETTING ONE USERNAME BY ID \n")
    # print(user)

    userJSON = user.as_dict()

    response['status'] = 200
    response['message'] = 'SUCCESS: GET BY ID'
    response['result'] = userJSON

    return jsonify(response)


@staticmethod
@users.route("/users/login", methods=['POST'])
def login():
    print("HELLO LADIES. LOGIN HERE. \n\n")

    email = request.form.get('email')
    passwordRaw = request.form.get('password')

    # CHECK WHETHER USER EXISTS OR NOT
    user2Check = User.query.filter_by(email=email).first_or_404()
    user2CheckJSON = user2Check.as_dict()

    # NOW, CHECK IF PASSWORD MATCH
    passwordMatchFlag = bcrypt.check_password_hash(user2CheckJSON['password'], passwordRaw)

    if (passwordMatchFlag == True):

        payload = {
            'email': user2CheckJSON['email'],
            'username': user2CheckJSON['username'],
            'userid': user2CheckJSON['id'],
            'propic': user2CheckJSON['image_file']
        }

        access_token = create_access_token(identity=payload)

        return jsonify(access_token=access_token), 200

    else:
        abort(401)


# @staticmethod
# @users.route("/users/changePassword", methods=['PUT'])
# @jwt_required
# def change_password():
#     print("HEWWO. TRYING TO CHANGE PASSWORD HERE! \n\n\n")

#     current_user = get_jwt_identity()

#     print(current_user)
#     return "YES"

@staticmethod
@users.route("/users/changeUsername", methods=['PUT'])
def change_username():

    token = request.headers.get('access_token')

    if(token in [None, '', ' ', " ", ""]):
        abort(401)

    payload = decode_token(token)['identity']

    currentUsername = request.form.get('current_username')
    newUsername = request.form.get('new_username')

    print("\n REALITY CHECK \n")
    print(currentUsername, newUsername)

    if(currentUsername == payload['username']):
        user = User.query.get_or_404(payload['userid'])
        user.username = newUsername

        user.save()

        userJSON = user.as_dict()

        response['status'] = 200
        response['message'] = 'SUCCESS: UPDATE USERNAME'
        response['result'] = userJSON

        return jsonify(response)
        # return "OK"
    
    else:
        abort(400)



@staticmethod
@users.route("/users/updatePropic", methods=['PUT'])
def update_propic():
    print("TRYING TO UPDATE PROPIC \n\n")

    token = request.headers.get('access_token')

    if(token in [None, '', ' ', " ", ""]):
        abort(401)

    payload = decode_token(token)['identity']

    user = User.query.get_or_404(payload['userid'])


    print("\n REALITY CHECK \n")

    propicNewRaw = request.files['propic_new']

    print(propicNewRaw)

    newPropicPath = save_picture(propicNewRaw)

    print("ISIT NEW? \n")
    print(newPropicPath)

    user.image_file = newPropicPath
    user.save()

    userJSON = user.as_dict()

    response['status'] = 200
    response['message'] = 'SUCCESS: UPDATE USERNAME'
    response['result'] = userJSON

    return jsonify(response)

    # return "YESSS"
    

    # if():

    #     user.save()

    #     userJSON = user.as_dict()

    #     response['status'] = 200
    #     response['message'] = 'SUCCESS: UPDATE USERNAME'
    #     response['result'] = userJSON

    #     return jsonify(response)
    #     # return "OK"
    
    # else:
    #     abort(400)



# @users.route("/reset_password", methods=['GET', 'POST'])
# def reset_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home'))
#     form = RequestResetForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         send_reset_email(user)
#         flash('An email has been sent with instructions to reset your password.', 'info')
#         return redirect(url_for('users.login'))
#     return render_template('reset_request.html', title='Reset Password', form=form)


# @users.route("/reset_password/<token>", methods=['GET', 'POST'])
# def reset_token(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('main.home'))
#     user = User.verify_reset_token(token)
#     if user is None:
#         flash('That is an invalid or expired token', 'warning')
#         return redirect(url_for('users.reset_request'))
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user.password = hashed_password
#         db.session.commit()
#         flash('Your password has been updated! You are now able to log in', 'success')
#         return redirect(url_for('users.login'))
#     return render_template('reset_token.html', title='Reset Password', form=form)