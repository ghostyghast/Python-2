import pandas as pd


def load(path: str):
    """load(str that represents path to csv file)
    function that loads csv file from given path and
    returns the dataframe object"""
    file = pd.read_csv(path)
    print('Loading dataset of dimensions', file.shape)
    return file
