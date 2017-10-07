import pandas as pd
from datascience import *


def transpose(tab):
    tab = tab.to_df().transpose()
    tab.columns = tab.iloc[0]
    return tab.drop(tab.index[0])
