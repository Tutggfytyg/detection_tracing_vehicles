from collections import Counter
from copy import copy
from pathlib import Path
from PIL import Image
import numpy as np
import cv2
import pandas as pd


class Image_statistic:
    def calculate_resolution_distribution(
        self,
        images_dir: Path,
    ) -> dict[tuple[int, int], int]:
        distribution = Counter()

        for image_path in images_dir.rglob("*"):
            if not image_path.is_file():
                continue

            with Image.open(image_path) as image:
                resolution = image.size  # (width, height)
            distribution[resolution] += 1

        return dict(distribution)

    def calculate_resolution_statistics(
        self,
        data_dir: Path,
    ) -> dict[tuple[int, int], dict[str, float]]:
        distribution = self.calculate_resolution_distribution(data_dir)

        total_images = sum(distribution.values())

        return {
            resolution: {
                "count": count,
                "percentage": count / total_images * 100,
            }
            for resolution, count in distribution.items()
        }


    def calculate_aspect_ratio_distribution(
        self,
        data_dir: Path,
    ) -> dict[float, int]:
        distribution = Counter()

        for image_path in data_dir.rglob("*"):
            if not image_path.is_file():
                continue

            with Image.open(image_path) as image:
                width, height = image.size

            aspect_ratio = round(width / height, 2)

            distribution[aspect_ratio] += 1

        return dict(distribution)


    def calculate_aspect_ratio_statistics(
        self,
        data_dir: Path,
    ) -> dict[float, dict[str, float]]:
        distribution = self.calculate_aspect_ratio_distribution(data_dir)

        total_images = sum(distribution.values())

        return {
            aspect_ratio: {
                "count": count,
                "percentage": round(count / total_images * 100, 2),
            }
            for aspect_ratio, count in distribution.items()
        }

    def calculate_brightness_distribution(
        self,
        data_dir: Path,
    ) -> dict[int, int]:
        distribution = Counter()

        for image_path in data_dir.rglob("*"):
            if not image_path.is_file():
                continue

            with Image.open(image_path) as image:
                image = image.convert("RGB")
                pixels = np.asarray(image, dtype=np.float32)

            luminance = (
                0.2126 * pixels[:, :, 0] # red
                + 0.7152 * pixels[:, :, 1] # green
                + 0.0722 * pixels[:, :, 2] # blue
            )

            brightness = round(float(luminance.mean()))

            distribution[brightness] += 1

        return dict(distribution)


    def brightness_category(self, data_dir: Path) -> dict[str, int]:
        brightness = self.calculate_brightness_distribution(data_dir)
        brightness_category = {}
        for brightness_num, brightness_count in brightness.items():
            if brightness_num < 64:
                brightness_category["dark"] = brightness_count
            if brightness_num < 128:
                brightness_category["medium"] = brightness_count
            if brightness_num < 192:
                brightness_category["bright"] = brightness_count
            if brightness_num > 192:
                brightness_category["very_bright"] = brightness_count
        return brightness_category


    def calculate_contrast(
        self,
        data_dir: Path,
    ) -> dict[int, int]:
        distribution = Counter()

        for image_path in data_dir.rglob("*"):
            if not image_path.is_file():
                continue

            with Image.open(image_path) as image:
                image = image.convert("RGB")
                pixels = np.asarray(image, dtype=np.float32)

            luminance = (
                0.2126 * pixels[:, :, 0] # red
                + 0.7152 * pixels[:, :, 1] # green
                + 0.0722 * pixels[:, :, 2] # blue
            )

            contrast = round(float(luminance.std()))

            distribution[contrast] += 1

        return dict(distribution)


    def calculate_blur_score(self, data_path: Path) -> dict[int, int]:

        distrubution = Counter()

        for image_path in data_path.rglob("*"):
            if not image_path.is_file():
                continue

            with Image.open(image_path) as image:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            laplacian = cv2.Laplacian(image, cv2.CV_64F)

            blur = float(laplacian.var())
            distrubution[blur] += 1

        return dict(distrubution)
