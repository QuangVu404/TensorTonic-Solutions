import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    Mean = float(np.mean(x))
    Median = float(np.median(x))

    count = Counter(x)
    Mode = count.most_common(1)[0][0]

    return Mean, Median, Mode