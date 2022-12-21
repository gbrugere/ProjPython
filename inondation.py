import pandas as pd
import pandas as pd
import geopandas as gpd 
import numpy as np 
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def adresse_to_gpd(df_adresse):
    return(gpd.GeoDataFrame(df_adresses, geometry=gpd.points_from_xy(df_adresses.lon, df_adresses.lat)))

#Coordonnées de l'habitation (en géometry) ->risque d'inondation
#gpd_adresses : tables geopandas qui contient les adresses du département
def adresse_to_geometry(dep,num,nom_voie,ville,code_postal):
  return(gpd_adresses[(gpd_adresses["numero"] == num) & (gpd_adresses["nom_commune"] == ville) & (gpd_adresses["nom_voie"] == nom_voie)]["geometry"])

#Fonction geometry ->risque 
def risque(geometry):
  risque=[]
  for k in range(len(df_risque_inond["geometry"])):
    if df_risque_inond["geometry"][k].contains(geometry):
      risque.append(df_risque_inond["scenario"][k])
  
  if len(risque)==0:
    return(3)
  
  elif risque[0]=="04Faicc_ct" or risque[0]=="04Fai":
    return(6)

  elif risque[0]=="03Mcc_ct" or risque[0]=="03Mcc":
    return(8)
  
  elif risque[0]=="02Moy":
    return(12)
  
  else : 
    return(18)

#Fonction finale
def adresse_to_risque(dep,num,nom_voie,ville,code_postal):
  return(risque(adresse_to_geometry(dep,num,nom_voie,ville,code_postal)))

