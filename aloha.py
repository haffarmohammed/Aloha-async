import numpy as np
from event import event


# retourne les machine occupées à l'instant T
def miseAJourMachinesOccupees(Echeancier, dureeTrans, T):
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
def simul(Echeancier, loiExpo, dureeTrans, k, lmbda, packetOfMachine):
    # Temps global
    Temps = 0

    # loiPoisson : tableu des valeurs aléatoires suivent la loi de poisson de paramétre lambda
    for i in loiExpo:
        # Récupérer les machines occupées à l'instant T
        machinesNotDispo = miseAJourMachinesOccupees(Echeancier, dureeTrans, Temps)

        # Si tous les machines sont occupées on avance le temps global jusqu'au il y aura au moin une machine libre
        while len(machinesNotDispo) == 10:
            Temps += np.random.exponential(lmbda, 1)[0]
            machinesNotDispo = miseAJourMachinesOccupees(Echeancier, dureeTrans, Temps)

        # Récupérer les machines disponibles
        machineDispo = []
        for m in range(10):
            if m not in machinesNotDispo:
                machineDispo.append(m)

        # Choisir d'un facon uniforme la prochaine machine qui va transmettre un paquet parmi les machines dispos
        machine = machineDispo[np.random.randint(0, len(machineDispo), 1)[0]]

        # Ajouter évènement à l'échéancier
        ptr = event(Temps, machine, packetOfMachine[machine])
        Echeancier.append(ptr)

        # Ajouter les copies du paquets à l'échéancier
        T_copis = 0
        for j in range(k - 1):
            T_copis += dureeTrans

            # trouver un instant avec un interval inter paquets qui suit la loi de poisson de paramètre k * lambda
            randInterval = np.random.exponential(k * lmbda, 1)[0]

            # Verifier si la machine et disponible à l'instant T + interval inter paquets
            machinesNotDispo = miseAJourMachinesOccupees(Echeancier, dureeTrans, Temps + T_copis + randInterval)
            # while machine in machinesNotDispo:
            #     print("a")
            #     randInterval += np.random.poisson(k * lmbda, 1)[0]
            #     machinesNotDispo = miseAJourMachinesOccupees(Echeancier, dureeTrans, Temps + T_copis + randInterval)

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
