from database.db import get_connection
from .entities.BusLine import BusLine
import simplejson as json
from flask import jsonify, request

class BusLineModel():

  @classmethod
  def add_busline(self, busline):
    try:
      connection = get_connection()

      with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO busline (id, name, fromm, too) 
              VALUES (%s,%s,%s,%s)""", (busline.id, busline.name, busline.fromm, busline.too)) 
        affected_rows = cursor.rowcount
        connection.commit()
      connection.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def delete_busline(self, busline):
    try:
      connection = get_connection()

      with connection.cursor() as cursor:
        cursor.execute("DELETE FROM busline WHERE  name = %s", (busline.name)) 
        affected_rows = cursor.rowcount
        connection.commit()
      connection.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)    