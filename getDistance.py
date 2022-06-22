from math import radians, cos, sin, asin, sqrt

def getDistance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    r = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2 
    c = 2 * asin(sqrt(a))

    distance = r * c
    return distance


