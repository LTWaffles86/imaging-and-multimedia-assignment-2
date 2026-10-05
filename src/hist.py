import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


def hist(ax: plt.Axes, array: npt.NDArray[np.uint8], color):
    ax.hist(array.ravel(), bins=256, range=(0, 255), color=color)
