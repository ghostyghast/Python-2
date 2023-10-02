from load_csv import load
import matplotlib.pyplot as plt


def main():
    """program that loads life_expectancy_years file
    and displays country information of a campus"""
    df = load('life_expectancy_years.csv')
    series = df.loc['Malaysia']
    plt.plot(series.index.astype(int), series.values)
    plt.xlabel('Life expectancy')
    plt.ylabel('Year')
    plt.title('Malaysia Life expectancy projections')
    plt.show()


if __name__ == '__main__':
    main()
