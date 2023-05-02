from flask import  Blueprint, request, jsonify
from utils.function_jwt import write_token,validate_token
#Entities
from models.entities.User import UserResive
#Models
from models.AuthModel import AuthModel


main = Blueprint('routes_auth', __name__)

@main.route('/logintest', methods=["POST"])
def logintest():
  try:
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
  except Exception as ex:
    return jsonify({'message': str(ex) }),500

@main.route('/login', methods=["POST"])
def login():
  try:

    dataRequest = request.get_json()
    name = dataRequest['user']
    password = dataRequest['password']


    data = UserResive(name, password)
    affected_data= AuthModel.verify_user(data)
    print(data.password, data.user)

    if affected_data != None:
      return jsonify({
        'status':'ok',
        'rol':affected_data.rol
      })
    else:
      return jsonify({'status': 'error'}), 401

  except Exception as ex:
      raise Exception(ex)

#@main.route("/verify/token")
#def verify_token():
#    print(request.headers['Authorization'].split("")[1])
#    return validate_token(token, output=True)
