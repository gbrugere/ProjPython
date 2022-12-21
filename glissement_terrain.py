import math 
import pandas as pd 


#Calcule la distance entre deux point repérés par leur latitude et leur longitude
def distance_lat_long(lat1, lat2, lon1, lon2):
     
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
      
    # Formule de Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
 
    c = 2 * math.asin(math.sqrt(a))
    
    # rayon de la terre
    r = 6371
      
    return(c * r)

#evenements à moins de 10km et datant de moins de 100 ans
def event_less_10km(lat1,lon1,df): 
                                #lat1 lon1 : latitude, longitude de l'habitation considérée
 
  dico={"distance":[],"date":[]}


  for k in range(len(df["longitudeDoublePrec"])):

    d=distance_lat_long(lat1,df["latitudeDoublePrec"][k],lon1,df["longitudeDoublePrec"][k])

    if d<=10 :

        dico["distance"].append(d)
        dico["date"].append(df["dateDebut"][k])
  
  return(dico)


def calcul_risque(dico): #dico : celui return par event_less_10km 

  risque=0
  quali_data=len(dico["date"]) #proportion d'event pour lasquelles on a la date/nb total d'event

  for k in range (len(dico["date"])):
    
    if type(dico["date"][k])!=str: #si aucune date n'est renseignée, on diminue la qualité totale de la donnée et on lui assigne l'année 1901

      annee=1901
      quali_data=quali_data-1

    else : 

      annee=int(dico["date"][k][:4])
                
    if 1900<=annee<=2022:

      risque=risque+(10-dico["distance"][k])*annee
  risque=(risque/2000000)*20 ##constante de normalisation trouvée en considérant le risque maximal observé

  if len(dico["date"])!=0:
    quali_data=quali_data/len(dico["date"])
    
  return (risque, quali_data)