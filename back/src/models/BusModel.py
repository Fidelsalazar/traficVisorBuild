from database.db import get_connection
from .entities.Bus import Bus
from datetime import datetime
from sys import argv
from os.path import exists
import simplejson as json
from flask import jsonify

class BusModel():

  @classmethod
  def get_bus_rtime(self):
    try:
      connection=get_connection()
      buslist=[]

      with connection.cursor() as cursor:
        cursor.execute("SELECT bus_id, bus_line, lat, lon, velocity FROM positionbus WHERE datatime = '2022-05-01 01:43:17'")
        row=cursor.fetchone()

        projects = []
        bus = None
        if row != None:
          bus=Bus(row[0],row[1],row[2],row[3],row[4])
          bus=bus.to_JESON()
        

      connection.close()
      return bus

    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def get_bus_time(self):
    
    try:
      connection=get_connection()
      buslist=[]

      with connection.cursor() as cursor:
        cursor.execute("SELECT bus_id, bus_line, lat, lon, velocity FROM positionbus WERE datetime = clock_timestamp()")
        resultset=cursor.fetchall()

        for row in resultset:
          bus=Bus(row[0],row[1],row[2],row[3],row[4])
          buslist.append(bus.to_JESON())
      
      connection.close()
      return buslist

    except Exception as ex:
      raise Exception(ex)
      
  @classmethod
  def get_bus(self):
    try:
      connection=get_connection()
      buslist=[]

      with connection.cursor() as cursor:
        cursor.execute("SELECT bus_id, bus_line, lat, lon, velocity FROM positionbus WHERE datatime = current_timestamp")
        
        resultset=cursor.fetchall()

        for row in resultset:
          bus=Bus(row[0],row[1],row[2],row[3],row[4])
          buslist.append(bus.to_JESON())
        
        geojson = {
           "type": "FeatureCollection",
            "features": [
            {
              "type": "Feature",
              "properties" : {
                "bus_id":d["bus_id"], 
                "bus_line":d["bus_line"], 
                "velocity":d["velocity"]
              },
              "geometry" : 
              {
                "type": "Point",
                "coordinates": [d["lat"], d["lon"]],
                
              }
              
            } for d in buslist]
        }

        outfile = '/home/fidel/Documentos/Tesis/trafico-master/output.geojson'
        output= open(outfile, 'w')
        json.dump(geojson,output)
        
      connection.close()
      return buslist

    except Exception as ex:
      raise Exception(ex)
  
