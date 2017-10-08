import pandas as pd
from datascience import *
import numpy as np


def transpose(tab):
    tab = tab.to_df().transpose()
    tab.columns = tab.iloc[0]
    return tab.drop(tab.index[0])

def bootstrap_median(original_sample, label, replications):
    '''
    Returns an array of bootstrapped sample medians:
    original_sample: table containing the original sample
    label: label of column containing the variable
    replications: number of bootstrap samples
    '''
    just_one_column = original_sample.select(label)
    medians = make_array()
    for i in np.arange(replications):
        bootstrap_sample = just_one_column.sample()
        resampled_median = percentile(50, bootstrap_sample.column(0))
        medians = np.append(medians, resampled_median)

    return medians