from flask import  Blueprint, jsonify,request
from time import sleep

#Entities
from models.entities.Bus import Bus

#Models
from models.BusModel import BusModel

main = Blueprint('bus_print', __name__)

@main.route('/')
def get_bus():
  try:
    buss = BusModel().get_bus()
    return jsonify(buss)
  except Exception as ex:
      return jsonify({'message':str(ex)}),500

@main.route('/time') 
def get_bus_time():
  while True:
    try:
      buss = BusModel().get_bus()
      if buss != None:
        return jsonify(buss)
      else:
        return jsonify({}), 404
    except Exception as ex:
      return jsonify({'message':str(ex)}),500
    sleep(0.1)

