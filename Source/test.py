from Modules import PlotDictionary
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)

x_ = np.linspace(0, 10, 1000)
y_ = np.sin(x_) + np.random.uniform(-0.2, 0.2, 1000)

plot_dict = {
    "data clean" : {
        "x" : x,
        "y" : y,
        "zorder" : 1
    },
    "data noisy" : {
        "x" : x_,
        "y" : y_,
        "ls" : "--",
        "zorder" : 1
    }
}

plotter = PlotDictionary(plot_dict)
plotter.plot_1d_series()
