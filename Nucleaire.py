import pandas as pd
import numpy as np

def conversion_radians(longitude,latitude):
    GPS_rad = ((longitude*np.pi)/180 , (latitude*np.pi)/180)
    return(GPS_rad)

#Calcul de la plus petite distance à une centrale nucléaire
def min_dist_centrales(long, lat, centrales) :
    d = np.inf
    k = 0
    for i in range(14) : #il y a 14 centrales nucleaires en FR
        long_centrale, lat_centrale = conversion_radians(centrales["Commune long"][i], centrales["Commune Lat"][i])
        D = 6371 * np.arccos(np.sin(lat_centrale)*np.sin(lat) + np.cos(lat_centrale)*np.cos(lat)*np.cos(long_centrale - long))
        if D<d :
            d = D
            k = i
    return(d,centrales["Centrale nuclaire"][k])

#Calcul du risque nucléaire
def risque_nucleaire(longitude, latitude, centrales):
    d_min, r = min_dist_centrales(longitude, latitude, centrales)
    if d_min <= 5 :
        return(20)
    elif d_min <= 20 :
        return(15)
    elif d_min <= 60 :
        return(10)
    elif d_min <= 100 :
        return(5)
    else :
        return(1)

def nucleaire(longitude, latitude, centrales):

    #Centrale nucléaire la plus proche, distance associé
    D, nearest_centrale = min_dist_centrales(longitude, latitude, centrales)
    print("La centrale nucleaire la plus proche se situe à :")
    print(D,nearest_centrale)

    #Mesure du risque nucléaire à cette adresse
    R = risque_nucleaire(longitude, latitude, centrales)
    print("Le risque nucléaire à cette adresse est de :")

    return(R)

