import pandas as pd
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


<<<<<<< HEAD
#Coordonnées de l'habitation (en géometry) ->risque d'inondation
#gpd_adresses : tables geopandas qui contient les adresses du département
def adresse_to_geometry(dep,num,nom_voie,ville,code_postal, gdp_adresses):
  return(gpd_adresses[(gpd_adresses["numero"] == num) & (gpd_adresses["nom_commune"] == ville) & (gpd_adresses["nom_voie"] == nom_voie)]["geometry"])
=======


def adresse_to_geometry_bis(dep,num,nom_voie,ville,code_postal):
  lon =df_adresse[(df_adresse["numero"] == num) & (df_adresse["nom_commune"] == ville) & (df_adresse["nom_voie"] == nom_voie)]["lon"]
  lat=df_adresse[(df_adresse["numero"] == num) & (df_adresse["nom_commune"] == ville) & (df_adresse["nom_voie"] == nom_voie)]["lat"]
  return(Point(lon,lat))
>>>>>>> 279790542acc269bbf80148fea6b9c6f93f7f465

#Fonction geometry ->risque
#Fonction geometry ->risque 
def risque(geometry,df_risque_inond):
  risque=[]
  for k in range(1,len(df_risque_inond["geometry"])):
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
def adresse_to_risque(dep,num,nom_voie,ville,code_postal,df_risque_inond):
  return(risque(adresse_to_geometry_bis(dep,num,nom_voie,ville,code_postal),df_risque_inond))

