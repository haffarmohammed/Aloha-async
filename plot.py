import plotly.figure_factory as ff
from matplotlib import pyplot as plt

from event import takeMachine, takeDate
import webbrowser as wb


# Plot des paquets
def show(Echeancier, dureeTrans, index):
    Echeancier.sort(key=takeMachine)

    df = []
    for e in Echeancier:
        df.append(dict(Task=str(e.machine), Start=str(int(e.date*10)),
                       Finish=str(int(e.date * 10 + dureeTrans)) , Resource='M' + str(e.machine)))

    colors = {'M0': 'rgb(180, 170, 160)',
              'M1': 'rgb(220, 0, 0)',
              'M2': 'rgb(0, 230, 40)',
              'M3': 'rgb(22, 110, 0)',
              'M4': 'rgb(20, 180, 100)',
              'M5': 'rgb(30, 20, 100)',
              'M6': 'rgb(60, 50, 40)',
              'M7': 'rgb(190, 80, 70)',
              'M8': 'rgb(120, 110, 0)',
              'M9': 'rgb(50, 140, 30)',
              }
    if len(df) > 0:
        fig = ff.create_gantt(df, colors=colors, index_col='Resource', group_tasks=True)
        # Enrigistrer dans un fichier HTML
        name = str(index) + ".html"
        fig.write_html(name)
        # Ouvrir dans un navigateur
        wb.open(name, 2)
    else:
        print("tous la paquets sont transmis")


def graphe():
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
