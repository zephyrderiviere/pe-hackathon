from common import *

#Calculs de stats en tout genre

print("Attributs disponibles : ", list(df.columns))
# print(str(df.head(3)))

print("Données de ", df.Date.min(), "à",  df.Date.max())
print("Nombre de lignes :", len(df))

valeurs_manquante = df.isna().sum()
print("Valeurs manquantes : \n",valeurs_manquante)