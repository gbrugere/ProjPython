

import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
import datetime

def get_annee(s):
  return(s[:4])


def get_week(s):
  week=datetime.date(int(s[:4]),int(s[5:7]),int(s[8:10])).isocalendar().week
  if week>=10:

    return(s[:4]+"W"+str(week))
  
  else:
    return(s[:4]+"W0"+str(week))

def preprocessing(df_temperature): #dep = département

    df_temperature=df_temperature[["Date","Température"]] #séléction de la série temporelle Température
    df_temperature["Annee"]=df_temperature["Date"].apply(lambda x:get_annee(x))
    df_temperature["Date"]=df_temperature["Date"].apply(lambda x: get_week(x)) #On extrait le jour de la table
    df_temperature=df_temperature.groupby(["Date"]).max() #On séléctionne la température maximale relevée au cours de la semaine
    df_temperature=df_temperature.dropna() #on supprimme les cellules vides
    df_temperature=df_temperature.sort_index() #on ordonne la table par date croissante

    return(df_temperature)

#vérification qu'on a bien 52 ou 53 mesures par ans (pour la saisonalité)
def test_saisonalité(df_temperature):

    for k in range (10,22):
        print(((df_temperature[df_temperature["Annee"] =="20"+str(k)].shape[0])==52) or ((df_temperature[df_temperature["Annee"] =="20"+str(k)].shape[0])==53))

#Temperature maximale journalière au cours du temps 
def plot_temperature(df_temperature):
    y=df_temperature[["Température"]]
    y.plot()
    f = plt.figure()
    f.set_figwidth(4)
    f.set_figheight(1)

    plt.show()
#décomposition de la série temporelle en composante saisonnelle, tendance et en bruit
def get_decomposition(df_temperature):
    y=df_temperature[["Température"]]
    decomposition = sm.tsa.seasonal_decompose(y, model='additive', period= 52)
    fig = decomposition.plot()
    plt.show()

#retourne les prédiction de temprérature pour un horizon donné, les paramètres du model sont pré rentrés. 
#model entrainé entre 2010 et 2019 et testé sur 2019, 2020, 2021, mi 2022
def get_prediction_graph(horizon,df_temperature): 
    y_train= df_temperature[:"2019W01"]["Température"]
    y=df_temperature["Température"]
    mod = sm.tsa.statespace.SARIMAX(y_train,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 53),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
    results = mod.fit()

    pred = results.get_prediction(start=472, end=horizon,dynamic=False)
    pred_ci = pred.conf_int()
    ax = y.plot(label='observed')
    pred.predicted_mean.plot(ax=ax, label='Forecast', alpha=.7, figsize=(14, 4))
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature')
    plt.legend()
    plt.show()

#retourne les prédiction de temprérature pour un horizon donné, les paramètres du model sont pré rentrés. 



