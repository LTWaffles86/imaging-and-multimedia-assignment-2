import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import PIL.ImageOps
from hist import hist
from PIL import Image

selfie_path = Path("images/selfie.jpg")
plots_path = Path("plots/")
if not plots_path.exists():
    os.mkdir(plots_path)

selfie_image: Image.Image = Image.open(selfie_path).convert("L")


def gamma_correct(image: Image.Image, gamma: float) -> Image.Image:
    gamma_lut: npt.NDArray[np.uint8] = (
        (np.linspace(0.0, 1.0, 256, dtype=np.float32) ** gamma * 255.0)
        .round()
        .clip(0, 255)
        .astype(np.uint8)
    )
    image_arr: npt.NDArray[np.uint8] = np.asarray(image)
    return Image.fromarray(gamma_lut[image_arr])


gamma_values = [0.25, 0.5, 1, 2, 4]

images_dir = Path("images/q3/")
if not images_dir.exists():
    os.mkdir(images_dir)

fig, axs = plt.subplots(2, (len(gamma_values) + 1) // 2)

images = [gamma_correct(selfie_image, gamma) for gamma in gamma_values]

for image, gamma in zip(images, gamma_values):
    image.save(
        images_dir.joinpath(
            (selfie_path.stem + "_" + str(gamma)).replace(".", "_")
        ).with_suffix(selfie_path.suffix)
    )

for image, ax in zip(images, axs):
    hist(ax, np.asarray(image), "gray")

equalized_image = PIL.ImageOps.equalize(selfie_image)
equalized_image.save(
    images_dir.joinpath(selfie_path.stem + "_equalized").with_suffix(selfie_path.suffix)
)
hist(axs[-1], np.asarray(equalized_image), "gray")

plt.savefig(plots_path.joinpath("gamma_histograms.svg"))
plt.show()
