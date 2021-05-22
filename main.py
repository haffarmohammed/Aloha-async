import numpy as np
import aloha as aloha
from IRSA import IRSApure
import matplotlib.pyplot as plt

from event import takeDate, takeMachine
from plot import graphe, show


class s():
    def __init__(self, lmbda, packetSauves):
        self.lmbda = lmbda
        self.packetSauves = packetSauves

    def __repr__(self):
        return "\nlambda: " + str(self.lmbda) + " ,Paquets sauvés: " + str(self.packetSauves)


# Définition des paramètres
kMax = 11
lambdaMax = 2
dureeTrans = 0.2
nbrMachine = 10
nbrPaquets = 1000


# Initialisation
Echeancier = []
Temps = 0
packetOfMachine = [1 for i in range(nbrMachine)]
stat = [[], []]
paquetSauves = 0
indexFile = 0



for l in np.arange(0.3, 0.64, 0.05):
    print('lambda: ' + str(l))
    for k in range(1, kMax):
        print('k: ' + str(k))

        # Générer la série des variable aléatoire de loi exponontiel avec paramètre lambda
        loiExpo = np.random.exponential(l, nbrPaquets)

        # Créer le scénario avec k copies pour chaque paquets
        aloha.simul(Echeancier, loiExpo, dureeTrans, k, l, packetOfMachine)

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

# # Générer la série des variable aléatoire de loi exponontiel avec paramètre lambda
# loiPoisson = np.random.exponential(1, nbrPaquets)
#
# # Créer le scénario avec k copies pour chaque paquets
# aloha.simul(Echeancier, loiPoisson, dureeTrans, 3, 0.1, packetOfMachine)
# # show(Echeancier, dureeTrans, 1)
#
# Echeancier.sort(key=takeMachine)
# print(Echeancier)

# paquetSauves = IRSApure(Echeancier, dureeTrans, indexFile)
#
# print(paquetSauves)

