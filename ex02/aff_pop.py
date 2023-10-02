from load_csv import load
import matplotlib.pyplot as plt


def check_num(num):
    """check_num(string of a number with a M,K or B suffix) -> str
    The function takes the num and removes the suffix and accordingly
    mulitplies the value, then returns it as a string"""
    if 'K' in num:
        num = num.replace('K', '')
        num = float(num) * 1000
    elif 'M' in num:
        num = num.replace('M', '')
        num = float(num) * 100000
    elif 'B' in num:
        num = num.replace('B', '')
        num = float(num) * 1000000000
    return str(int(num))


def main():
    """Program that plots two countries's information
    one one same graph, along with a legend"""
    df = load('population_total.csv')
    country1 = df.loc['Belgium', :'2050']
    country2 = df.loc['France', :'2050']
    country2 = country2.apply(check_num)
    country1 = country1.apply(check_num)
    plt.plot(country1.index.astype(int), country1.values.astype(int))
    plt.plot(country2.index.astype(int), country2.values.astype(int))
    ticks, values = plt.yticks()
    plt.yticks(ticks, [f"{int(x / 100000)}M" for x in ticks])
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.legend(['Belgium', 'France'], loc='lower right')
    plt.show()


if __name__ == '__main__':
    main()
