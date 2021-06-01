from decimal import Decimal, ROUND_HALF_UP

import numpy as np
import IRSA as aloha
from SIC import IRSApure
import matplotlib.pyplot as plt
from plot import generateGraphe

# ============= Définition des paramètres =================
# k repetitions des paquets
kMax = 16
# durée de transfert d'un paquet
dureeTrans = 0.2
# nombre de machines
nbrMachine = 10
# nombre de paquets à genérer pour faire la simulation
nbrPaquets = 400
# nombre d'itérations
iterations = 10

# ============== Initialisation ============================
# tableau qui stocque les paquets générés
Echeancier = []
# l'instant T du temps
Temps = 0
# un tableau de taille de nombre des machine, chaque cas i stocke l'indice du dernier paquet transmis par la machine i
packetOfMachine = [1 for i in range(nbrMachine)]
# tableau de 2 dimensions stocke les statistique des résultats de simulation
stat = [[], []]
# nombre de paquets sauvés pour chaque simulation (paquets qui a au moins une copies sans collision)
paquetSauves = 0
arr = []

# boucle pour varier lambda
for l in np.arange(1.0, 3.0, 0.3):
    print("lambda = " + str(Decimal(l).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
    # boucle pour varier k
    for k in range(1, kMax):
        print('k: ' + str(k))
        # boucle pour faire i iteration de chaque couple (lambda, k) puis calculer la moyenne de toutes les iterations
        for i in range(1, iterations):
            # Genérer la série des variable aléatoire de loi exponontiel avec paramètre lambda
            loiExpo = np.random.exponential(1 / l, nbrPaquets)
            # Créer le scénario avec k copies pour chaque paquets
            aloha.createScenario(Echeancier, loiExpo, dureeTrans, k, l, packetOfMachine)
            # Appliquer l'algorithme de SIC
            paquetSauves = IRSApure(Echeancier, dureeTrans)
            # Sauvegarder les résultats
            arr.append(paquetSauves)
            Echeancier = []

        stat[0].append(k)
        # calculer la moyenne des paquets sauvés pour le couple (lambda, k)
        print("AVG = " + str(np.array(arr).mean()))
        stat[1].append(np.array(arr).mean())
        arr.clear()

    paquetSauves = 0
    # Ajouter une nouvelle courbe pour lambda
    plt.plot(stat[0], stat[1], label="lambda = " + str(Decimal(l).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
    stat[0] = []
    stat[1] = []

# Sauvegarde et afficher le graphe
generateGraphe()
