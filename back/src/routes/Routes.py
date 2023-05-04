import json
from flask import  Blueprint, jsonify,request
import uuid
#Entities
from models.entities.BusLine import BusLine
#Models
from models.BusLineModel import BusLineModel
from models.PointsModel import PointsModel
from models.StopsModel import StopsModel

main = Blueprint('rutes_print', __name__)

@main.route('/add', methods=['POST'])
def add_points():
  try:
    #print(request.json)
    data = request.get_json()
    rute = data['route']
    stops = data['stops']
    mod_form = data['modForm']

    name = mod_form['name']
    fromm = mod_form['fromm']
    to = mod_form['too']
    print(name, fromm, to, rute, stops)

    id = uuid.uuid4()

    busline = BusLine(str(id),name, fromm, to)
    affected_rows = BusLineModel.add_busline(busline)

    if affected_rows == 1:
      buslineid = busline.id
      print(buslineid)
      affected_rows_points = PointsModel.add_points(rute, buslineid)
      affected_rows_stops = StopsModel.add_stops(stops,buslineid)
      if affected_rows_points != 0 and affected_rows_stops >= 0 :
        return jsonify({
          'status':'ok'
        })
    else:
      return jsonify({'message':"Error on insert"}),500
  except Exception as ex:
    return jsonify({'message': str(ex) }),500

@main.route('/get', methods=['POST'])
def get_busline_points():
  try:
    print(request.json)
    data = request.get_json()
    search = data['search']
    print(search)

    if 'search' not in data:
      return jsonify({'message': 'Search key not found in request JSON'}), 400

    datareturn= PointsModel.get_busroute(search)
    print(datareturn.response)

    if datareturn is not None :
      return datareturn
    else:
      return jsonify({'message':"Error on insert"}),500
  except Exception as ex:
    return jsonify({'message': str(ex) }),500

'''@main.route('/delete/<busline>', methods=['DELETE'])
def delete_points(busline):
  try:
    route = Points(busline)

    affected_rows = BusLineModel.delete_points(route)

    if affected_rows == 1:
      return jsonify(route.id)
    else:
      return jsonify({'message':"Error on delete"}),404
  except Exception as ex:
    return jsonify({'message': str(ex) }),500'''
'''
try:
    connection = get_connection()

    with connection.cursor() as cursor:
        # Verificar que buslineid existe en la tabla busline
        cursor.execute("SELECT id FROM busline WHERE id=%s", (buslineid,))
        result = cursor.fetchone()
        if result is None:
            # Si buslineid no existe, lanzar una excepción
            raise ValueError("El ID de la línea de autobús no existe en la tabla busline")

        # Insertar los puntos de la parada en la tabla stops
        for point in stops:
            id = uuid.uuid4()
            id_str = str(id)
            lat = point['lat']
            lng = point['lng']
            cursor.execute("""INSERT INTO stops (ID, latitud, longitud, busline)
                            VALUES (%s,%s,%s,%s)""", (id_str, lat, lng, buslineid ))
        affected_rows = cursor.rowcount
        connection.commit()
    connection.close()
    return affected_rows
except Exception as ex:
    raise Exception(ex)

'''
