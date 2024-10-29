# fichier commun à charger à chaque exécution afin que chaque membre aie la même DataFrame

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import sklearn.cluster as cluster


NUMBER_OF_CLUSTERS = 100


def create_clusters(n):
    kmeans = cluster.KMeans(n).fit(df[['Latitude', 'Longitude']])
    return kmeans


df = pd.read_csv("./data/earthquake.csv")

df["Date"] = pd.to_datetime(df["Date"] + " " + df["Time"], format="%m/%d/%Y %H:%M:%S")
df.drop("Time", axis = 1, inplace=True)

#Ajout d'une catégorie représenant le groupe

df['GeoGroup'] = create_clusters(NUMBER_OF_CLUSTERS).labels_
df['GeoGroup'].astype(int)
