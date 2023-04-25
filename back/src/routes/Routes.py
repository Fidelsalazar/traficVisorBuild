from flask import  Blueprint, jsonify,request
#Entities
from models.entities.Points import Points
#Models
from models.PointsModel import PointsModel

main = Blueprint('busline_print', __name__)

@main.route('/add', methods=['POST']) 
def add_points():
  try:
    #print(request.json)
    #id=request.json['id']
    lat=request.json['latitud']
    lon=request.json['longitud']
    busline=request.json['busline']
    
    route = Points("{"+latitud+"}", "{"+longitud+"}", "{"+busline+"}")

    affected_rows = PointsModel.add_points(route)

    if affected_rows == 1:
      return jsonify(route.id)
    else:
      return jsonify({'message':"Error on insert"}),500  
  except Exeption as ex:
    return jsonify({'message': str(ex) }),500

@main.route('/delete/<busline>', methods=['DELETE']) 
def delete_points(busline):
  try:
    route = Points(busline)

    affected_rows = BusLineModel.delete_points(route)

    if affected_rows == 1:
      return jsonify(route.id)
    else:
      return jsonify({'message':"Error on delete"}),404  
  except Exeption as ex:
    return jsonify({'message': str(ex) }),500

