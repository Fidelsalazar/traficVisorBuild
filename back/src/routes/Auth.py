from flask import  Blueprint, request, jsonify
from utils.function_jwt import write_token,validate_token


main = Blueprint('routes_auth', __name__)

@main.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    if data['user']== "fidelsalazar990923@gmail.com" and data['password']=="1234": 
        token =  write_token(data=request.get_json())
        return jsonify({
            'status':'ok',
            'rol': 'admin'
        }) 
    if data['user']=="danicgd@gmail.com" and data['password']=="1234":
        return jsonify({
            'status':'ok',
            'rol': 'user'
        })       
    else:
        response = jsonify({
            "message":"User not found"
        })
        response.status_code = 404
        return response

@main.route("/verify/token")
def verify_token():
    print(request.headers['Authorization'].split("")[1])
    return validate_token(token, output=True)
