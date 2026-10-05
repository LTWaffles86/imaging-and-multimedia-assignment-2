import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from hist import hist
from PIL import Image

image_path = Path("images/selfie.jpg")
plots_path = Path("plots/")
selfie_image = Image.open(image_path).convert("RGB")

image_array = np.asarray(selfie_image)
colors = ["red", "green", "blue"]

fig, axs = plt.subplots(1, 3)


for ax, channel, color in zip(axs, np.moveaxis(image_array, 2, 0), colors):
    hist(ax, channel, color)

if not plots_path.exists():
    os.mkdir(plots_path)
plt.savefig(plots_path.joinpath("color_channels_hist.svg"))
plt.show()

luma = np.average(image_array, axis=2)

fig, ax = plt.subplots()
hist(ax, luma, "gray")
plt.savefig(plots_path.joinpath("grayscale_hist.svg"))
plt.show()
