import pandas as pd


def load(path: str) :
    file = pd.read_csv(path)
    print('Loading dataset of dimensions', file.shape)
    return file
