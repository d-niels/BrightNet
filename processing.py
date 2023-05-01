import numpy as np


def high_pass_filter(arr: np.array, cutoff: float, replace: float = 0):
    """
    Applies a high pass filter to an array. Anything below the cutoff is 0.

    Inputs:
        arr (np.array): the input array to be filtered
        cutoff (float): the cutoff value
        replace (float): the value that replacing below the filter

    Outputs:
        None
    """
    arr = arr.where(arr > cutoff, replace, arr)


def low_pass_filter(arr: np.array, cutoff: float, replace: float = 0):
    """
    Applies a low pass filter to an array. Anything above the cutoff is 0.

    Inputs:
        arr (np.array): the input array to be filtered
        cutoff (float): the cutoff value
        replace (float): the value that replaces anything above the cutoff

    Outputs:
        None
    """
    arr = arr.where(arr < cutoff, replace, arr)


def calculate_light(m: np.array, c: float = 0):
    """
    Calculates the amount of light given an apparent magitude

    Inputs:
        m (np.array): apparent magnitude of the object
        c (float): absolute magnitude of the object

    Outputs:
        float: amount of light
    """
    return np.power(10, (c - m) / 2.5).sum()

