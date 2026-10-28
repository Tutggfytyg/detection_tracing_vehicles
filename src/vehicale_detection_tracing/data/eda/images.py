from pathlib import Path
from collections import Counter
from PIL import Image
import numpy as np
import cv2


class Images_EDA:
    def get_images_paths(
        self, data_path: Path, supported_image_extentions: list[str]
    ) -> list[Path]:
        return [
            path
            for path in data_path.rglob("*")
            if path.is_file() and path.suffix.lower() in supported_image_extentions
        ]

    def count_images(
        self, data_path: Path, supported_image_extentions: list[str]
    ) -> int:
        return len(self.get_images_paths(data_path, supported_image_extentions))

    def count_img_by_extentions(
        self, data_path: Path, supported_image_extentions: list[str]
    ):
        counts = Counter(
            path.suffix.lower()
            for path in self.get_images_paths(data_path, supported_image_extentions)
        )

        return dict(sorted(counts.items()))

    def count_resolution_distribution(
        self, data_path: Path, supported_image_extentions: list[str]
    ) -> dict[tuple[int], int]:
        img_resol_distribution = Counter()

        for image_path in self.get_images_paths(data_path, supported_image_extentions):
            with Image.open(image_path) as image:
                resolution = image.size  # (width, height)
            img_resol_distribution[resolution] += 1

        sorted_img_resol_distribution = sorted(img_resol_distribution)
        return dict(sorted_img_resol_distribution)

    def count_aspect_ratio_disctribution(
        self, data_path: Path, supported_image_extentions: list[str]
    ) -> dict[tuple[int], int]:

        aspect_ratio_distrib = Counter()

        for image_path in self.get_images_paths(data_path, supported_image_extentions):
            with Image.open(image_path) as image:
                width, height = image.size
                aspect_ratio = width / height
            aspect_ratio_distrib[aspect_ratio] += 1

        return aspect_ratio_distrib

    def count_channels_distribution(
        self, data_path: Path, supported_image_extentions: list[str]
    ) -> dict[tuple[str], int]:
        channels_distr = Counter()

        for image_path in self.get_images_paths(data_path, supported_image_extentions):
            with Image.open(image_path) as image:
                channels_distr[image.mode] += 1

        return channels_distr

    def culculate_luminance(self, pixels: np.float32):
        return (
            0.2126 * pixels[:, :, 0]  # red
            + 0.7152 * pixels[:, :, 1]  # green
            + 0.0722 * pixels[:, :, 2]  # blue
        )

    def count_brightness_distribution(
        self, data_path: Path, supported_ext: list[str]
    ) -> dict[int, int]:
        distribution = Counter()

        for image_path in self.get_images_paths(data_path, supported_ext):
            with Image.open(image_path) as image:
                if image.mode != "RGB":
                    image = image.convert("RGB")
                pixels = np.asarray(image, dtype=np.float32)

                luminance = self.culculate_luminance(pixels)

            brightness = round(float(luminance.mean()))
            distribution[brightness] += 1

        return distribution

    def count_contrast_distribution(
        self, data_path: Path, supported_ext: list[str]
    ) -> dict[int, int]:
        distribution = Counter()

        for image_path in self.get_images_paths(data_path, supported_ext):
            with Image.open(image_path) as image:
                if image.mode != "RGB":
                    image = image.convert("RGB")
                pixels = np.asarray(image, dtype=np.float32)

            luminance = self.culculate_luminance(pixels)
            contrast = round(float(luminance.std()))
            distribution[contrast] += 1

        return distribution

    def count_blur_score_distribution(
        self, data_path: Path, supported_ext: list[str]
    ) -> dict[float, int]:

        distrubution = Counter()

        for image_path in self.get_images_paths(data_path, supported_ext):
            image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
            laplacian = cv2.Laplacian(image, cv2.CV_64F)
            blur = float(laplacian.var())
            blur = round(blur)
            distrubution[blur] += 1

        return distrubution
