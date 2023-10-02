import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load('population_total.csv')
    Belgium = df.loc['Belgium', :'2050']
    france = df.loc['France', :'2050']
    fra
    print(france)
    plt.plot(Belgium.index.astype(int), Belgium.values.astype(int))
    plt.plot(france.index.astype(int), france.values.astype(int))
    plt.yticks()
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.legend(['Belgium', 'France'], loc='lower right')
    plt.show()


if __name__ == '__main__':
    main()
