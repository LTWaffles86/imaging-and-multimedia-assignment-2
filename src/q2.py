import os
from pathlib import Path

import numpy as np
import numpy.typing as npt
from PIL import Image

pixel_values = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255)]
color_names = ["red", "green", "blue", "black", "white"]


def count_pixels(image: Image.Image, color: tuple[int, int, int]) -> int:
    pixels: npt.NDArray[np.uint8] = np.asarray(image)
    return (pixels == color).all(axis=2).sum()


def make_color_images() -> None:
    rows = 256
    cols = 256
    for pixel_value, name in zip(pixel_values, color_names):
        arr = np.zeros((rows, cols, 3), np.uint8)
        arr[:, :] = pixel_value
        image: Image.Image = Image.fromarray(arr)
        image.save(image_path.joinpath(name).with_suffix(".png"))


def pixel_report(image_path: Path) -> list[int]:
    image: Image.Image = Image.open(image_path).convert("RGB")
    return [count_pixels(image, pixel) for pixel in pixel_values]


image_path = Path("images")
if not image_path.exists():
    os.mkdir(image_path)

make_color_images()

headers = ["Filepath"] + color_names
column_widths = [20] + [5] * len(color_names)
for header, width in zip(headers, column_widths):
    print(f"{header:<{width}}", end=" ")
print()

for file_path in image_path.iterdir():
    print(f"{file_path!s:{column_widths[0]}}", end=" ")
    report = pixel_report(file_path)
    for count, width in zip(report, column_widths[1:]):
        print(f"{count:>{width}}", end=" ")
    print()
