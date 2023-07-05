from typing import Callable
import numpy as np

def calculate(values: list) -> dict:
    """Takes a list of 9 integers and splits them into a list of lists, each 
    containing three integers. Then, it converts the list of lists into a 3x3 
    Numpy array. Finally, the function calculates the max, min and sum along 
    both the x and y-axis, as well as a flattened matrix, and returns a 
    dictionary with the aggregate statistics."""
    def calculation_matrix(func: Callable[[np.ndarray], np.ndarray]) -> list:
        """Takes the 3x3 Numpy array, carries out an aggregate function across 
        the x and y-axes and as a flattened matrix. Finally, it returns a list 
        of three numbers."""
        return [[func(array[:3, 0]), func(array[:3, 1]), func(array[:3, 2])],
                [func(array[0, :3]), func(array[1, :3]), func(array[2, :3])],
                func(array)]
    
    if len(values) == 9:
        array = np.array([[num for num in values[:3]], 
                          [num for num in values[3:6]], 
                          [num for num in values[6:len(values)]]])
    else: 
        raise ValueError("List must contain nine numbers.")
    calculations = {}
    agg_statistics = {"mean": np.mean, "variance": np.var, 
                      "standard deviation": np.std, "max": np.amax, 
                      "min": np.amin, "sum": np.sum}
    for stat_name, agg_func in agg_statistics.items():
        calculations[stat_name] = calculation_matrix(agg_func)
    return calculations
