from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from hist import hist

image_path = Path("images/selfie.jpg")
selfie_image = Image.open(image_path).convert("RGB")

image_array = np.asarray(selfie_image)
colors = ["red", "green", "blue"]

fig, axs = plt.subplots(1, 3)


for ax, channel, color in zip(axs, np.moveaxis(image_array, 2, 0), colors):
    hist(ax, channel, color)
plt.show()

luma = np.average(image_array, axis=2)

fig, ax = plt.subplots()
hist(ax, luma, "gray")
plt.show()
