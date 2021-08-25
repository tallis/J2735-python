from math import radians, cos, sin, asin, sqrt, modf


def nmea2deg(coordinate):

    splitCoordinate = str(coordinate).split(".")
    degree = splitCoordinate[0][0:-2]

    minutesCoordinate = splitCoordinate[0][-2:] + "." + splitCoordinate[1]
    division = float(minutesCoordinate) / 60

    # 6 decimal places for higher precision -- perhaps too much
    division = '%.6f' % round(division, 6)
    return int(degree) + float(division)


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return (km * 1000)



