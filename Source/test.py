from Modules import PlotDictionary
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)

x_ = np.linspace(0, 10, 1000) + np.random.random(1000) / 4
y_ = np.sin(x_)

plot_dict = {
    "data clean" : {
        "x" : x,
        "y" : y
    },
    "data noisy" : {
        "x" : x_,
        "y" : y_
    }
}

plotter = PlotDictionary(plot_dict)
plotter.plot_1d_series()
