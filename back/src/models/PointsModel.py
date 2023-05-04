from flask import jsonify, make_response
from database.db import get_connection
import uuid
#Entities
from models.entities.Points import GetPoints


class PointsModel():

  @classmethod
  def add_points(self, route, buslineid:str):

    try:
      connection = get_connection()

      with connection.cursor() as cursor:
        for point in route[0]:
          id = uuid.uuid4()
          id_str = str(id)
          print()
          lat = point['lat']
          lng = point['lng']
          cursor.execute("""INSERT INTO points (ID, latitud, longitud, busline)
              VALUES (%s,%s,%s,%s)""", (id_str, lat, lng, buslineid ))
        affected_rows = cursor.rowcount
        connection.commit()
      connection.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def get_busroute(self, search):
    try:
        connection = get_connection()

        route = []
        stops = []

        with connection.cursor() as cursor:
          cursor.execute("""SELECT id FROM busline WHERE name = %s""", (search,))
          row = cursor.fetchone()

          if row is not None:
            busline_id = row[0]
            cursor.execute("""SELECT latitud, longitud FROM points WHERE busline = %s""", (busline_id,))
            points = cursor.fetchall()
            for rows in points:
              point = GetPoints(rows[0], rows[1])
              route.append(point.to_JSON())

            cursor.execute("""SELECT latitud, longitud FROM stops WHERE busline = %s""", (busline_id,))
            stopoints = cursor.fetchall()
            for rowst in stopoints:
              points = GetPoints(rowst[0], rowst[1])
              stops.append(points.to_JSON())

            response = make_response(jsonify({
            'stops': stops,
            'points': route
            }))
            response.headers['Content-Type'] = 'application/json'
            return response
          else:
            return jsonify({'message': 'Error on insert'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
