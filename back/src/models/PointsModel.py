from database.db import get_connection
from .entities.Points import Points
import simplejson as json
from flask import jsonify, request

class BusLineModel():

  @classmethod
  def add_busline(self, busline):
    try:
      connection = get_connection()

      with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO points (ID, latitud, longitud, busline) 
              VALUES (%s,%s,%s,%s)""", (points.id, points.name, points.fromm, points.too)) 
        affected_rows = cursor.rowcount
        connection.commit()
      connection.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)