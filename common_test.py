# fichier commun à charger à chaque exécution afin que chaque membre aie la même DataFrame
# pour les tests (chargement plus rapide)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/earthquakes_min.csv")
