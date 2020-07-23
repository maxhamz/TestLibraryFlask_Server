from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)
errMsg = {
    'status': 500,
    'message': "INTERNAL SERVER ERROR"
}


@errors.app_errorhandler(400)
def error_400(error):
    errMsg['status'] = 400
    errMsg['message'] = 'BAD REQUEST'
    return jsonify(errMsg), 400


@errors.app_errorhandler(401)
def error_401(error):
    errMsg['status'] = 401
    errMsg['message'] = 'ACCESS UNAUTHORIZED'
    return jsonify(errMsg), 401


@errors.app_errorhandler(404)
def error_404(error):
    errMsg['status'] = 404
    errMsg['message'] = 'NOT FOUND'
    return jsonify(errMsg), 404


@errors.app_errorhandler(500)
def error_500(error):
    return jsonify(errMsg), 500