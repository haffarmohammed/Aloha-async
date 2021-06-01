from matplotlib import pyplot as plt


def generateGraphe():
    # naming the x axis
    plt.xlabel('K')
    # naming the y axis
    plt.ylabel('paquets transmis')

    # giving a title to my graph
    plt.title('Asynchrone Aloha Statistics')

    # show a legend on the plot
    plt.legend()

    plt.savefig('graphe.png')
    # function to show the plot
    plt.show()
