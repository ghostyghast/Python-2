# import pandas as pd
from load_csv import load
from matplotlib import pyplot as plt


def main():
    """Program that displays the projection of life expectancy
    in relation to the gross national product
    of the year 1900 for each country"""
    income = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_expect = load('life_expectancy_years.csv')
    plt.plot(income.loc[:, '1900'].astype(int),
             life_expect.loc[:, '1900'], 'o')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.xscale('log')
    plt.title('1900')
    plt.xticks([300, 1000, 10000], ['300', '1K', '10K'])
    plt.show()


if __name__ == '__main__':
    main()
