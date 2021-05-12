# Ordonner par numero de machine
def takeMachine(elem):
    return elem.machine

# Ordonner par date
def takeDate(elem):
    return elem.date


class event():
    def __init__(self, date, machine, packet):
        self.date = date
        self.machine = machine
        self.packet = packet

    def __repr__(self):
        return "\nDate: " + str(self.date) + " ,machine:" + str(self.machine) + " ,packet:" + str(self.packet)



