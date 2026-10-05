from pathlib import Path

import numpy as np
from PIL import Image

pixel_values = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255)]
color_names = ["red", "green", "blue", "black", "white"]
image_path = Path("images")


def count_pixels(image: Image.Image, color: tuple[int, int, int]):
    pixels = np.asarray(image)
    return np.count_nonzero(np.all(pixels[:, :] == color, axis=2))


def make_color_images():
    rows = 256
    cols = 256
    for pixel_value, name in zip(pixel_values, color_names):
        arr = np.zeros((rows, cols, 3), np.uint8)
        arr[:, :] = pixel_value
        image: Image.Image = Image.fromarray(arr)
        image.save(image_path.joinpath(name).with_suffix(".png"))


def pixel_report(image: Path):
    image: Image.Image = Image.open(image).convert("RGB")
    for pixel, name in zip(pixel_values, color_names):
        print(name, "pixels :", count_pixels(image, pixel))


make_color_images()

for file_path in image_path.iterdir():
    print(file_path)
    pixel_report(file_path)
