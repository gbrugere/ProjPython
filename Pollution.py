import pandas as pd
import numpy as np
from math import *

def distance_lat_long(lat1, lat2, lon1, lon2):

    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Formule de Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))

    # rayon de la terre
    r = 6371

    return(c * r)


def site_polluant_plus_proche(lat, long, df):
    acc =df["code site"][0]
    d = distance_lat_long(lat, long, df["Latitude"][0], df["Longitude"][0])
    val = df["valeur"][0]
    n = len(df)
    for i in range(n):
        d2 = distance_lat_long(lat, long, df["Latitude"][i], df["Longitude"][i])
        if d2 < d:
            acc = df["code site"][i]
            d = d2
            val = df["valeur brute"][i]
    return(acc, d2, val)

def risque_polution(lat, long, df_polCO, df_polSO2, df_polPM10):
    sCO, dCO, valCO = site_polluant_plus_proche(lat, long, df_polCO)
    sSO2, dSO2, valSO2 = site_polluant_plus_proche(lat, long, df_polSO2)
    sPM10, dPM10, valPM10 = site_polluant_plus_proche(lat, long, df_polPM10)

    if valPM10 < 5:
        risPM10 = 0
    elif 5 <= valPM10 and valPM10 < 10:
        risPM10 = 2
    elif 10 <= valPM10 and valPM10 < 20:
        risPM10 = 4
    elif 20 <= valPM10 and valPM10 < 30:
        risPM10 = 5
    else:
        risPM10 = 7

    if valCO < 0.01:
        risCO = 0
    elif 0.01 <= valCO and valCO < 0.3:
        risCO = 2
    elif 0.3 <= valCO and valCO < 0.7:
        risCO = 4
    elif 0.7 <= valCO and valCO < 1.2:
        risCO = 5
    else:
        risCO = 6


    if valSO2 < 1:
        risSO2 = 0
    elif 1 <= valSO2 and valSO2 < 5:
        risCO = 2
    elif 5 <= valSO2 and valSO2 < 8:
        risCO = 4
    elif 8 <= valSO2 and valSO2 < 15:
        risSO2 = 5
    else:
        risSO2 = 7

    return(risSO2 + risCO + risPM10)