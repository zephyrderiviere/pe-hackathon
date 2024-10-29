from common import *

#Calculs de stats en tout genre

print("Attributs disponibles : ", list(df.columns))
# print(str(df.head(3)))

print("Données de ", df.Date.min(), "à",  df.Date.max())
print("Nombre de lignes :", len(df))

valeurs_manquante = df.isna().sum()
print("Valeurs manquantes : \n",valeurs_manquante)

x = df.groupby("Type")["Magnitude"].describe()

#df.groupby("Type")["Magnitude"].mean().plot(yerr = [df.groupby("Type")["Magnitude"].quantile(0.25),df.groupby("Type")["Magnitude"].quantile(0.75)]).set_ylim(0,7)
graf = x["mean"].plot(yerr = [x["mean"]-x["25%"], x["75%"]-x["mean"]], ylabel = "Magnitude",kind ="bar", xlabel="Source de la secousse", title="Magnitude en fonction de la source de la secousse")
graf.set_xticks([0,1,2,3],x.index, rotation = "horizontal")
graf.set_ylim(bottom = 0, top =7.5)

plt.show()