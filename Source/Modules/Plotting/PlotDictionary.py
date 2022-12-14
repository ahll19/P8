import matplotlib.pyplot as plt
import numpy as np


class PlotDictionary:
    def __init__(self, plotting_dict: dict) -> None:
        for key, value in plotting_dict.items():
            assert type(value) == dict, "plotting_dict should be nested dictionaries"
        
        self.plot_dict = plotting_dict
    
    
    def plot_1d_series(self):
        self.__check_inputs()
    
    
    def __check_inputs(self):
        for key_outer, value_outer in self.plot_dict.items():
            assert type(value_outer["x"]) == np.array, "Sub-dictionaries must contain key 'x' with value of type np.array"
            assert type(value_outer["y"]) == np.array, "Sub-dictionaries must contain key 'y' with value of type np.array"
