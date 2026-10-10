from pathlib import Path
from PIL import Image
import numpy as np


class Image_Validation:
    def get_images_paths(
        self, data_path: Path, supported_images_extentions: list[str]
    ) -> list[Path]:
        return [
            path
            for path in data_path.rglob("*")
            if path.is_file() and path.suffix.lower() in supported_images_extentions
        ]

    def num_of_total_images(
        self, data_path: Path, supported_images_extention: list[str]
    ) -> int:
        return len(self.get_images_paths(data_path, supported_images_extention))

    def readableness_image_validation(
        self, data_path: Path, supported_images_extention: list[str]
    ) -> list[str] | bool:
        unreadable_images = []
        images_paths = self.get_images_paths(data_path, supported_images_extention)

        for image_path in images_paths:
            try:
                with Image.open(image_path) as image:
                    image.verify()

                # Actually decode the image data.
                with Image.open(image_path) as image:
                    image.load()

            except OSError, SyntaxError, ValueError:
                unreadable_images.append(str(image_path))

        if unreadable_images:
            return unreadable_images
        else:
            return True

    def dimensions_validation(
        self,
        data_path: Path,
        supported_images_extention: list[str],
        expected_ratio: float,
    ) -> list[str] | bool:
        wrong_dimensions = []
        images_paths = self.get_images_paths(data_path, supported_images_extention)

        for image_path in images_paths:
            with Image.open(image_path) as image:
                width, height = image.size

            ratio = width / height
            if ratio != expected_ratio:
                wrong_dimensions.extend([str(ratio), str(image_path)])

        if not wrong_dimensions:
            return True
        else:
            return wrong_dimensions

    def channels_validation(
        self,
        data_path: Path,
        supported_images_extention: list[str],
        expected_channels: int,
    ) -> list[str] | bool:
        wrong_channel_num = []
        images_paths = self.get_images_paths(data_path, supported_images_extention)

        for image_path in images_paths:
            with Image.open(image_path) as image:
                current_num_of_channels = len(image.getbands())
                if current_num_of_channels != expected_channels:
                    wrong_channel_num.extend(
                        [str(current_num_of_channels), str(image_path)]
                    )

        if not wrong_channel_num:
            return True
        else:
            return wrong_channel_num

    def images_dtype_validation(
        self,
        data_path: Path,
        supported_images_extention: list[str],
        expected_dtype: np.dtype,
    ) -> bool | list[str]:

        invalid_dtype = []
        images_paths = self.get_images_paths(data_path, supported_images_extention)

        for image_path in images_paths:
            with Image.open(image_path) as image:
                image_array = np.asarray(image)

            current_image_dtype = image_array.dtype
            if current_image_dtype != expected_dtype:
                invalid_dtype.extend([str(current_image_dtype), str(image_path)])

        if not invalid_dtype:
            return True
        else:
            return invalid_dtype

    def color_formats_validation(
        self,
        data_path: Path,
        supported_images_extention: list[str],
        expected_color_format: str,
    ) -> list[str] | bool:
        invalid_color_formats = []
        images_paths = self.get_images_paths(data_path, supported_images_extention)

        for image_path in images_paths:
            with Image.open(image_path) as image:
                current_color_format = image.mode
                if current_color_format != expected_color_format:
                    invalid_color_formats.extend(
                        [current_color_format, str(image_path)]
                    )

        if not invalid_color_formats:
            return True
        else:
            return invalid_color_formats
