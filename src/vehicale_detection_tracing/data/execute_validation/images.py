from pathlib import Path
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path
from src.vehicale_detection_tracing.data.validation.images import Image_Validation
from src.vehicale_detection_tracing.data.execute_validation.pattern import Valindation_Template
import numpy as np


class Execute_Images_Validation(Image_Validation, Valindation_Template):
    def __init__(self, train_path: Path, test_path: Path, supported_extetions: list[str]) -> None:
        self.train_path = train_path
        self.test_path = test_path
        super().__init__()
        self.train_total = self.num_of_total_images(self.train_path, supported_extetions)
        self.test_total = self.num_of_total_images(self.test_path, supported_extetions)


    def execute_readableness_image_validation(self, train_path: Path, test_path: Path, supported_ext: list[str]) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.readableness_image_validation(train_path,supported_ext)
        test_set_res = self.readableness_image_validation(test_path,supported_ext)
        error_msg = "unreadable images"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)



    def logging_readableness_image_validation_res(self, train_path: Path, test_path: Path, supported_ext: list[str])-> None:
        val_result = self.execute_readableness_image_validation(train_path, test_path, supported_ext)
        val_type = "image readablness"
        self.logging_blank(val_result, val_type)



    def execute_dimensions_validation(
        self,
        train_path: Path,
        test_path: Path,
        supported_ext : list[str],
        expected_ratio: float
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.dimensions_validation(
            train_path, supported_ext, expected_ratio
        )
        test_set_res = self.dimensions_validation(
            test_path, supported_ext, expected_ratio
        )

        error_msg = "invalid dimentions"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)


    def logging_dimentions_validation_res(
        self,
        train_path: Path,
        test_path: Path,
        supported_ext: list[str],
        expected_ratio: float
    ) -> None:
        val_result = self.execute_dimensions_validation(
            train_path, test_path, supported_ext, expected_ratio
        )
        type_of_val = "dementions"
        self.logging_blank(val_result, type_of_val)



    def execute_channels_validation(
        self, train_path: Path, test_path: Path, supported_ext: list[str], expected_channels: int
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.channels_validation(train_path, supported_ext, expected_channels)
        test_set_res = self.channels_validation(test_path, supported_ext, expected_channels)
        error_msg = "invalid channels"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)


    def logging_channels_validation_res(
        self, train_set_path: Path, test_set_path: Path,supported_ext: list[str], expected_channels: int
    ) -> None:
        val_result = self.execute_channels_validation(
            train_set_path, test_set_path,supported_ext, expected_channels
        )
        type_of_val = "channels"
        self.logging_blank(val_result, type_of_val)


    def execute_images_dtype_validation(
        self, train_path: Path, test_path: Path, supported_ext: list[str], expected_dtype: np.dtype
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.images_dtype_validation(train_path, supported_ext, expected_dtype)
        test_set_res = self.images_dtype_validation(test_path, supported_ext, expected_dtype)
        error_msg = "invalid data type"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)


    def logging_image_dtype_valiadtion_res(
        self, train_path: Path, test_path: Path,supported_ext: list[str], expected_dtype: np.dtype
    ) -> None:
        val_result = self.execute_images_dtype_validation(
            train_path, test_path, supported_ext, expected_dtype
        )
        type_of_val = "dtype"
        self.logging_blank(val_result, type_of_val)


    def execute_color_formats_validation(self, train_path: Path, test_path: Path, supported_ext: list[str], color_formats: str) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.color_formats_validation(train_path, supported_ext, color_formats)
        test_set_res = self.color_formats_validation(test_path, supported_ext, color_formats)
        error_msg = "wrong color format"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)



    def logging_color_formats_validation_res(self, train_path: Path, test_path: Path, supported_ext: list[str], color_format: str) -> None:
        val_res = self.execute_color_formats_validation(train_path, test_path, supported_ext, color_format)
        val_type = "color format"
        self.logging_blank(val_res, val_type)

if __name__ == "__main__":
    supported_img_ext = [".jpg"]
    expected_ratio = 1.7777777777777777
    channels_num = 3
    img_dtype = np.uint8
    expected_color_format = "RGB"

    img_val = Execute_Images_Validation(train_set_path, test_set_path, supported_img_ext)
    img_val.logging_readableness_image_validation_res(train_set_path, test_set_path, supported_img_ext)
    img_val.logging_dimentions_validation_res(train_set_path, test_set_path, supported_img_ext, expected_ratio)
    img_val.logging_channels_validation_res(train_set_path, test_set_path,supported_img_ext, channels_num)
    img_val.logging_image_dtype_valiadtion_res(train_set_path, test_set_path, supported_img_ext, img_dtype)
    img_val.logging_color_formats_validation_res(train_set_path, test_set_path, supported_img_ext, expected_color_format)
