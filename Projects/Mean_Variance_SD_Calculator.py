# Solution to the Freecodecamp Data Analysis with Python Project "Mean-Variance-Standard Deviation Calculator"

import numpy as np


def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("Input list must contain exactly 9 digits")
    input_array = np.array(input_list).reshape((3, 3))
    result = {
        "mean": [
            list(input_array.mean(axis=0)),
            list(input_array.mean(axis=1)),
            input_array.mean().item(),
        ],
        "variance": [
            list(input_array.var(axis=0)),
            list(input_array.var(axis=1)),
            input_array.var().item(),
        ],
        "standard deviation": [
            list(input_array.std(axis=0)),
            list(input_array.std(axis=1)),
            input_array.std().item(),
        ],
        "max": [
            list(input_array.max(axis=0)),
            list(input_array.max(axis=1)),
            input_array.max().item(),
        ],
        "min": [
            list(input_array.min(axis=0)),
            list(input_array.min(axis=1)),
            input_array.min().item(),
        ],
        "sum": [
            list(input_array.sum(axis=0)),
            list(input_array.sum(axis=1)),
            input_array.sum().item(),
        ],
    }
    return result
