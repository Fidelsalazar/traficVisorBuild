from flask import  Blueprint, jsonify,request
import uuid
#Entities
from models.entities.BusLine import BusLine
#Models
from models.BusLineModel import BusLineModel

main = Blueprint('busline_print', __name__)

@main.route('/add', methods=['POST'])
def add_busline():
  try:
    #print(request.json)
    name = request.json['name']
    fromm = request.json['fromm']
    to = request.json['too']
    id = uuid.uuid4()
    print(id)

    busline = BusLine(str(id),name, fromm, to)

    affected_rows = BusLineModel.add_busline(busline)

    if affected_rows == 1:
      return jsonify(busline.id)
    else:
      return jsonify({'message':"Error on insert"}),500
  except Exception as ex:
    return jsonify({'message': str(ex) }),500

@main.route('/get', methods=['GET'])
def get_busline():
  try:
    routess = BusLineModel().get_busline()

    if routess != None:
      return jsonify({
        'status': 'ok',
        'routes': routess
      })
    else:
      return jsonify({}),404

  except Exception as ex:
    return jsonify({'message': str(ex) }),500

@main.route('/delete/<name>', methods=['DELETE'])
def delete_busline(name):
  try:
    busline = BusLine(name)

    affected_rows = BusLineModel.delete_busline(busline)

    if affected_rows == 1:
      return jsonify(busline.id)
    else:
      return jsonify({'message':"Error on delete"}),404
  except Exception as ex:
    return jsonify({'message': str(ex) }),500

