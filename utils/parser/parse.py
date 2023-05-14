import gpxpy
import gpxpy.gpx
from django.contrib.gis.geos import Point, LineString
import math
from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import Point

# Parsing an existing file:
# -------------------------

def parse_gpx(gpxfile):
    gpx_file = gpxfile

    gpx = gpxpy.parse(gpx_file)

    storage_array = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                pnt = Point(point.latitude, point.longitude, point.elevation)
                storage_array.append(pnt)
    
    ls = LineString(storage_array)
    return(ls)

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

def naive_elevation(linestring):

    steps = []
    dist = 0
    for i in range(len(linestring.coords)-1):
        start = linestring[i]
        end = linestring[i+1]
        lat1 = start[0]
        lat2 = end[0]
        lon1 = start[1]
        lon2 = end[1]

        step = haversine(lon1, lat1, lon2, lat2)
        dist += step
        steps.append(dist)


    zarray =    []
    for point in linestring.coords:
        zarray.append(point[2])

    endpoint = len(zarray)
    ele = 0
    for z in range(endpoint-1):
        z0= zarray[z]
        z1 = zarray[z+1]
        delta = z1-z0 
        if delta > 0:
            ele += delta
    return [ele, zarray, steps]
    # There are many more utility methods and functions:
    # You can manipulate/add/remove tracks, segments, points, waypoints and routes and
    # get the GPX XML file from the resulting object:


def leafletBoundsToPoly(bounds):
            ne = bounds['_northEast']
            sw = bounds['_southWest']

            west = float(sw['lng'])
            east = float(ne['lng'])

            north = float(ne['lat'])
            south = float(sw['lat'])
  
            geom = Polygon(( (north, west), (north, east), (south, east),(south, west),(north, west)))
            return geom