import numpy as np
import pandas as pd

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])

def get_rue_corect(s,df_adresse):
    rue=df_adresse["nom_voie"].drop_duplicates().tolist()
    min=levenshtein(s,rue[0])
    dist=levenshtein(s,rue[0])
    index_dist=0

    for k in range(1,len(rue)):
        dist=levenshtein(s,rue[k])
        if dist <min :
            min =dist 
            index_dist=k
 

    return(rue[index_dist])

def get_ville_correct(s,df_adresse):
    ville=df_adresse["nom_commune"].drop_duplicates().tolist()
    min=levenshtein(s,ville[0])
    dist=levenshtein(s,ville[0])
    index_dist=0

    for k in range(1,len(ville)):
        dist=levenshtein(s,ville[k])
        if dist <min :
            min =dist 
            index_dist=k
 

    return(ville[index_dist])