# fichier commun à charger à chaque exécution afin que chaque membre aie la même DataFrame
# pour les tests (chargement plus rapide)

import numpy as np
import pandas as pd

df = pd.read_csv("./earthquakes_min.csv")

