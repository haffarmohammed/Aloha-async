def IRSApure(Echeancier, dureeTrans, packetSauves=0):
    packetNotInConflict = []
    conflict = 0

    while True:
        # extraire les packets sans conflit
        for e1 in Echeancier:
            for e2 in Echeancier:
                if (e2.date <= e1.date < e2.date + dureeTrans or e2.date < e1.date + dureeTrans <= e2.date + dureeTrans) and e1 != e2:
                    conflict = 1
                    break
            if conflict == 0:
                contains = 0
                for e in packetNotInConflict:
                    if e1.packet == e.packet and e1.machine == e.machine:
                        contains = 1
                if contains == 0:
                    packetNotInConflict.append(e1)
            else:
                conflict = 0

        # MAJ du nombre de paquets transmis avec succès
        packetSauves += len(packetNotInConflict)

        # [Condition d'arrét] si il n'y a pas de paquets à sauver, on sort du boucle
        if len(packetNotInConflict) == 0:
            break

        arr = Echeancier.copy()
        # Supprimer les paquet sans conflit et ses copies
        for e2 in Echeancier:
            for e1 in packetNotInConflict:
                if e1.machine == e2.machine and e1.packet == e2.packet:
                    if e2 in arr:
                        arr.remove(e2)
        Echeancier = arr.copy()
        arr.clear()

        packetNotInConflict.clear()

    print(packetSauves)
    return packetSauves
