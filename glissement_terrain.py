import math 
import pandas as pd 


#prend une adresse comme argument et retourne les coordonnées GPS
def adresse_to_gps(dep,num,nom_voie,ville,code_postal):

    adresses_dep = pd.read_csv("/Users/corentinpla/Downloads/Adresses/adresses-"+str(dep)+".csv", sep=";") #recuperation des adresses postales correspondant au département de l'utilisateur
    
    foyer_infos = adresses_dep[(adresses_dep["numero"] == num) & (adresses_dep["nom_commune"] == ville) & (adresses_dep["nom_voie"] == nom_voie)] 
    foyer = foyer_infos.to_numpy()
    foyer = foyer.tolist()
    print(foyer) #informations sur le domicile de l'utilisateur

    #Coordonnees geographiques du dommicile 
    lo = foyer[0][12]
    la = foyer[0][13]

    return([lo, la])



#Calcule la distance entre deux point repérés par leur latitude et leur longitude
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

#evenements à moins de 10km et datant de moins de 100 ans
def event_less_10km(lat1,lon1): 
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

      annee=int(df["dateDebut"][k][:4])
                
    if 1900<=annee<=2022:

      risque=risque+(10-dico["distance"][k])*annee
  
  quali_data=quali_data/len(dico["date"])
    
  return (risque, quali_data)