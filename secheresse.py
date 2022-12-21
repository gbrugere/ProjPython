import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx

def secheresse(dep,num,nom_voie,ville,code_postal):

  #Récupération des données concernant le domicile de l'utilisateur
  adresses_dep = pd.read_csv("https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-"+dep+".csv.gz", compression='gzip', sep=";", error_bad_lines=False) #recuperation des adresses postales correspondant au département de l'utilisateur
  foyer_infos = adresses_dep[(adresses_dep["numero"] == num) & (adresses_dep["nom_commune"] == ville) & (adresses_dep["nom_voie"] == nom_voie)]

  df_secheresse = gpd.read_file("DataSets/AleaRG"+dep+"_L93/AleaRG"+dep+"_L93.shp") #dataframe contenant les zones arigleuses du département donné
  df_secheresse.to_csv() #conversion du fichier en csv


  #Calcul du score moyen de "sécheresse" (i.e. niveau de gonflement/retrait d'argile, échelle de 1 à 3) du département considéré
  argile_dep = np.mean(df_secheresse["niveau"])

  #Conversion des coordonnées GPS d'un point en une géométrie exploitable sur Geopandas
  geometry = gpd.points_from_xy(foyer_infos["lon"], foyer_infos["lat"])

  #Création des dataframe avec geométrie du point à localiser
  geo_foyer = gpd.GeoDataFrame(foyer_infos, crs="EPSG:4326", geometry=geometry)
  geo_foyer.crs
  #print(geo_foyer) #TEST

  df_1 = df_secheresse[df_secheresse.niveau == 1]
  df_2 = df_secheresse[df_secheresse.niveau == 2]
  df_3 = df_secheresse[df_secheresse.niveau == 3]
  df_1.crs
  df_2.crs
  df_3.crs
  df_secheresse.crs

  #print(df_secheresse.head()) #TEST

  #Cartographie des zones de sécheresse (selon le degré de gonflement/retrait des argiles) dans le département 31
  fig,ax = plt.subplots(figsize=(10, 10))
  df_1.to_crs(3857).plot(ax = ax, color ='yellow', alpha = 0.6,zorder=2)
  df_2.to_crs(3857).plot(ax = ax, color ='orange', alpha = 0.6,zorder=2)
  df_3.to_crs(3857).plot(ax = ax, color ='red', alpha = 0.6,zorder=2)
  geo_foyer.to_crs(3857).plot(ax=ax, color="black",zorder=2)
  ax.set_title("Cartographie des zones de sécheresse préocupantes en Haute-Garonne")
  fig.legend()
  ctx.add_basemap(ax=ax,source=ctx.providers.OpenStreetMap.Mapnik)
  plt.show()

  #Fonction position géographique de l'habitation -> risque sécheresse précis associé


<<<<<<< HEAD
  print("Le score de sécheresse (de 1 à 5) de l'habitation est de :"+str(argile_dep*(5/3)))
  return(argile_dep*(5/3))
=======
  print("Le score de sécheresse (de 1 à 5) de l'habitation est de :"+str(argile_dep))
  return(argile_dep)
#
>>>>>>> 3b691532d7418558f60fc76726701857b49592c8
