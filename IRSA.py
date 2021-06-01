import numpy as np
from event import event


# retourne les machine occupées à l'instant T
def MajMachinesOccupees(Echeancier, dureeTrans, T):
    MNotdispo = []

    if len(Echeancier) == 0:
        return []
    else:
        s = 0
        while s < len(Echeancier):
            # trouver les machine occupés dans l'intervat [T, T + la durée de transition d'un paquet]
            if Echeancier[s].date + dureeTrans > T >= Echeancier[s].date or \
                    Echeancier[s].date < T + dureeTrans <= Echeancier[s].date + dureeTrans:

                # Si la mchine n'etait pas déja occupée, on l'ajoute à "MNotdispo"
                if Echeancier[s].machine not in MNotdispo:
                    MNotdispo.append(Echeancier[s].machine)
            s += 1
        return MNotdispo


# Créer le scénarion
def createScenario(Echeancier, loiExpo, dureeTrans, k, unSurLambda, packetOfMachine):
    # Temps global
    Temps = 0

    # loiExpo : tableu des valeurs aléatoires suivent la loi exponentiel de paramètre lambda
    for i in loiExpo:
        # Récupérer les machines occupées à l'instant T
        machinesNotDispo = MajMachinesOccupees(Echeancier, dureeTrans, Temps)

        # Si tous les machines sont occupées on avance le temps global jusqu'il y aura au moins une machine libre
        while len(machinesNotDispo) == 10:
            Temps += np.random.exponential(unSurLambda, 1)[0]
            machinesNotDispo = MajMachinesOccupees(Echeancier, dureeTrans, Temps)

        # Récupérer les machines disponibles
        machineDispo = []
        for m in range(10):
            if m not in machinesNotDispo:
                machineDispo.append(m)

        # Choisir d'une facon uniforme la prochaine machine qui va transmettre un paquet parmi les machines disponibles
        machine = machineDispo[np.random.randint(0, len(machineDispo), 1)[0]]

        # Ajouter évènement à l'échéancier
        ptr = event(Temps, machine, packetOfMachine[machine])
        Echeancier.append(ptr)

        # Ajouter les copies du paquets à l'échéancier
        T_copis = 0
        for j in range(k - 1):
            T_copis += dureeTrans

            # trouver un instant avec un interval inter paquets qui suit la loi exponentiel de paramètre 1/(k * lambda)
            randInterval = np.random.exponential(unSurLambda / k, 1)[0]

            # Avancer le temps
            T_copis += randInterval

            # Ajouter la copie à l'écheancier
            ptr = event(Temps + T_copis, machine, packetOfMachine[machine])
            Echeancier.append(ptr)

            machinesNotDispo.clear()

        # MAJ du nombre de paquets transmis par la machine i
        packetOfMachine[machine] += 1

        # Avancer le temps global
        Temps += i

        machinesNotDispo.clear()
