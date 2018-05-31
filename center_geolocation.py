#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from math import cos, sin, atan2, sqrt, pi, radians, degrees


def center_geolocation(geolocations):
    x = 0
    y = 0
    z = 0
    lenth = len(geolocations)
    for lon, lat in geolocations:
        lon = radians(float(lon))
        lat = radians(float(lat))

        x += cos(lat) * cos(lon)
        y += cos(lat) * sin(lon)
        z += sin(lat)

    x = float(x / lenth)
    y = float(y / lenth)
    z = float(z / lenth)

    return (degrees(atan2(y, x)), degrees(atan2(z, sqrt(x * x + y * y))))


if __name__ == '__main__':
    locations = [[121.627179,31.216703],[121.605026,31.259052],[121.45656,31.298815],[121.334574,31.200171],
        [121.398733,31.160907],[121.492668,31.180334],[121.531599,31.19347],[121.499531,31.166234],[121.59282,31.207169]]
    print(center_geolocation(locations))
