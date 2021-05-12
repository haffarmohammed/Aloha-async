import numpy as np
import aloha as aloha
from IRSA import IRSApure
import matplotlib.pyplot as plt

from plot import graphe


class s():
    def __init__(self, lmbda, packetSauves):
        self.lmbda = lmbda
        self.packetSauves = packetSauves

    def __repr__(self):
        return "\nlambda: " + str(self.lmbda) + " ,Paquets sauvés: " + str(self.packetSauves)


# Définition des paramètres
kMax = 20
lambdaMax = 10
dureeTrans = 3
nbrMachine = 10
nbrPaquets = 100


# Initialisation
Echeancier = []
Temps = 0
packetOfMachine = [1 for i in range(nbrMachine)]
stat = [[], []]
paquetSauves = 0
indexFile = 0
np.random.seed(3)


for l in range(1, lambdaMax):
    print('lambda: ' + str(l))
    for k in range(1, kMax):
        print('k: ' + str(k))

        # Générer la série des variable aléatoire de loi de poisson avec paramètre lambda
        loiPoisson = np.random.poisson(l, nbrPaquets)

        # Créer le scénario avec k copies pour chaque paquets
        aloha.simul(Echeancier, loiPoisson, dureeTrans, k, l, packetOfMachine)

        # Appliquer l'algorithme de l'IRSA / SIC
        paquetSauves = IRSApure(Echeancier, dureeTrans, indexFile)

        # Sauvegarder les résultats
        stat[0].append(k)
        stat[1].append(paquetSauves)

        Echeancier = []
    paquetSauves = 0

    # Ajouter une nouvelle courbe pour lambda
    plt.plot(stat[0], stat[1], label="lambda = " + str(l))

    stat[0] = []
    stat[1] = []

# Sauvegarde et afficher le graphe
graphe()
