import pandas as p
import matplotlib.pyplot as plt

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def importData():
    miasta = p.read_csv(r'C:\Users\mwicki\Downloads\miasta.csv')
    print(miasta)
    miasta = p.concat(
        [miasta, p.DataFrame([{"Rok": 2010, "Gdansk": 460, "Poznan": 555, "Szczecin": 405}])]
        , ignore_index=True
    )
    print(miasta)
    miasta = miasta.set_index('Rok')
    plt.figure()
    plt.subplot(211) #2 - amount of plots, 1 - column, 1 - row
    plt.plot(miasta.index, miasta["Gdansk"], 'ro', miasta.index, miasta["Gdansk"], 'r')
    plt.title('Ludność miast')
    plt.xlabel('Rok')
    plt.ylabel('Ludność w tys.')
    plt.subplot(212) #2 - amount of plots, 1 - column, 2 - row
    plt.plot(miasta.index, miasta, 'ro', miasta.index, miasta)
    plt.title('Ludność miast')
    plt.xlabel('Rok')
    plt.ylabel('Ludność w tys.')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    importData()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
