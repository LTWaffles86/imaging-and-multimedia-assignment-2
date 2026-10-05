import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from PIL import Image

from hist import hist

image_path = Path("images/Shapes.png")
image: Image.Image = Image.open(image_path).convert("L")


def gamma_correct(image: Image.Image, gamma: float) -> Image.Image:
    gamma_lut: npt.NDArray[np.uint8] = (
        (np.linspace(0.0, 1.0, 256, dtype=np.float32) ** gamma * 255.0)
        .round()
        .clip(0, 255)
        .astype(np.uint8)
    )
    image_arr = np.asarray(image)
    return Image.fromarray(gamma_lut[image_arr])


gamma_values = [0.25, 0.5, 1, 2, 4]

image_path = Path("images/q3/")
if not image_path.exists():
    os.mkdir(image_path)

fig, axs = plt.subplots(1, len(gamma_values))

images = [gamma_correct(image, gamma) for gamma in gamma_values]

for image, gamma in zip(images, gamma_values):
    image.save(
        image_path.joinpath(
            (image_path.stem + "_" + str(gamma)).replace(".", "_")
        ).with_suffix(".jpg")
    )

for image, ax in zip(images, axs):
    hist(ax, np.asarray(image), "gray")

plt.show()
