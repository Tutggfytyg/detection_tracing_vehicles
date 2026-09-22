from pathlib import Path
from src.logger import logger
from PIL import Image
import cv2
import numpy as np


class Image_validation:
    def dimensions_validation(
        self, data_dir: Path, expected_width: int, expected_height: int
    ) -> list[Path] | bool:
        wrong_dimensions = []

        for file_path in data_dir.rglob("*"):
            if not file_path.is_file():
                continue

            try:
                with Image.open(file_path) as image:
                    width, height = image.size

                if width != expected_width or height != expected_height:
                    wrong_dimensions.append(file_path)

            except (OSError, SyntaxError, ValueError) as error:
                logger.error("error %s", error)

        if len(wrong_dimensions) == 0:
            return True

        return wrong_dimensions

    def channels_validation(
        self, data_dir: Path, expected_channels: int
    ) -> list[Path] | bool:
        wrong_channel_num = []

        for file_path in data_dir.rglob("*"):
            if not file_path.is_file():
                continue

            try:
                with Image.open(file_path) as image:
                    if len(image.getbands()) != expected_channels:
                        wrong_channel_num.append(file_path)

            except (OSError, SyntaxError, ValueError) as error:
                logger.error("error %s", error)

        if len(wrong_channel_num) == 0:
            return True

        return wrong_channel_num

    def images_dtype_validation(
        self, data_dir: Path, expected_dtype: type
    ) -> bool | list[Path]:

        invalid_dtype = []

        for file_path in data_dir.rglob("*"):
            if not file_path.is_file():
                continue

            try:
                with Image.open(file_path) as image:
                    image_array = np.asarray(image)

                if image_array.dtype != expected_dtype:
                    invalid_dtype.append(file_path)

            except (OSError, SyntaxError, ValueError) as error:
                logger.error("error %s", error)

        if len(invalid_dtype) == 0:
            return True

        return invalid_dtype

    def color_formats_validation(
        self, data_dir: Path, expected_color_format: str
    ) -> list[Path] | bool:
        invalid_color_formats = []

        for file_path in data_dir.rglob("*"):
            if not file_path.is_file():
                continue

            try:
                with Image.open(file_path) as image:
                    if image.mode != expected_color_format:
                        invalid_color_formats.append(file_path)

            except (OSError, SyntaxError, ValueError) as error:
                logger.error("error %s", error)

        if len(invalid_color_formats) == 0:
            return True

        return invalid_color_formats
