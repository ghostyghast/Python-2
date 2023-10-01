from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """program that loads life_expectancy_years file
    and displays country information of a campus"""
    df = load('life_expectancy_years.csv')
    series = df.loc[df['country'] == 'France']
    print(series)
    # plt.plot(series.values, series.index)
    # plt.xlabel = 'Life expectancy'
    # plt.ylabel = 'Year'
    # plt.title = 'France Life expectancy projections'
    # plt.show()

if __name__ == '__main__':
    main()
