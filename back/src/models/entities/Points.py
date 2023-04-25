class Bus():

  def __init__(self, id, latitud=None, longitud=None, busline=None)-> None:
    self.id=id
    self.busline=busline
    self.lat=latitud
    self.lon=longitud

  def to_JESON(self):
    return{
      'id':self.id,
      'bus_line':self.bus_line,
      'lat':self.lat,
      'lon':self.lon,
    }