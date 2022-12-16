import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


class PlotDictionary:
    __plot_1d_series_arguments = {
        "x" : [np.ndarray],
        "y" : [np.ndarray],
        "zorder" : [int],
        "alpha" : [float, int],
        "ls" : [str],
        "lw" : [float, int],
        "marker" : [str],
        "marker_size" : [float, int],
        "c" : [str] 
    }
    
    def __init__(self, plotting_dict: dict, backend: str = "TkAgg") -> None:
        error_string = "plotting_dict should be nested dictionaries"
        for key, value in plotting_dict.items():
            assert type(value) == dict, error_string
        
        self.plot_dict = plotting_dict
        self.backend = backend
    
    
    def plot_config(self, grid: bool = False):
        pass
    
    
    def plot_1d_series(self):
        self.__check_inputs()
        
        mpl.use(self.backend)
        
        fig, ax = plt.subplots()
        
        for outer_key, inner_dict in self.plot_dict.items():
            ax.plot(
                inner_dict.pop("x"),
                inner_dict.pop("y"),
                label=outer_key,
                **inner_dict
            )
        
        fig.legend()
        plt.tight_layout()
        plt.show()
    
    
    def __check_inputs(self):
        for outer_key, inner_dict in self.plot_dict.items():
            for inner_key, value in inner_dict.items():
                # make sure each dict contains x and y values
                error_string = f"Dictionaries must contain \"x\" and \"y\" " \
                                + f"keys, but missing one in dictionary " \
                                + f"\"{outer_key}\""
                x_in = "x" in inner_dict.keys()
                y_in = "y" in inner_dict.keys()
                assert x_in and y_in, error_string
                
                # Check that all keys are valid
                error_string = f"Key {inner_key} found in dictionary "\
                                + f"{outer_key} but method only accepts"\
                                +f"{self.__plot_1d_series_arguments.keys()}"
                correct_key = inner_key in self.__plot_1d_series_arguments
                assert correct_key, error_string
            
                # check that all types are valid
                valid_value_types = self.__plot_1d_series_arguments[inner_key]
                value_type = type(value)
                error_string = f"Dictionary {outer_key} has key " \
                                + f"\"{inner_key}\" with invalid type " \
                                + f"{value_type}. Only accepts types " \
                                + f"{valid_value_types}"
                correct_type = value_type in valid_value_types
                assert correct_type, error_string
