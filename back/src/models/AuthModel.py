from database.db import get_connection
from .entities.User import UserResponse
from datetime import datetime
from sys import argv
from os.path import exists
import simplejson as json
from flask import jsonify, request

class AuthModel():

  @classmethod
  def verify_user(self, data):
    try:

      connection=get_connection()

      with connection.cursor() as cursor:
        cursor.execute("SELECT name, password, rol FROM users WHERE name = %s",(data.user,))
        row=cursor.fetchone()

        userData = None
        if row != None and row[1] == data.password:
          userData=UserResponse(row[2])
          userData.to_JSON()


      connection.close()
      return  userData

    except Exception as ex:
      return jsonify({'error': str(ex)}), 500
