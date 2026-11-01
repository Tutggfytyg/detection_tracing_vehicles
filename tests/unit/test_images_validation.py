import pytest
from src.vehicale_detection_tracing.data.validation.images import Image_Validation


class Test_Img_Validation(Image_Validation):
    @pytest.mark.unit
    def test_valid_image_is_accepted(self, valid_rgb_image, supp_img_ext):
        assert self.readableness_image_validation(valid_rgb_image.parent, supp_img_ext)

    @pytest.mark.unit
    def test_valid_image_ratio_is_accepted(
        self, valid_rgb_image, supp_img_ext, supp_img_ratio
    ):
        assert self.dimensions_validation(
            valid_rgb_image.parent, supp_img_ext, supp_img_ratio
        )

    @pytest.mark.unit
    def test_corrupt_image_is_rejected(self, corrupt_image, supp_img_ext):
        result = self.readableness_image_validation(corrupt_image.parent, supp_img_ext)
        assert isinstance(result, list)

    @pytest.mark.unit
    def test_wide_image_is_rejected(self, wide_image, supp_img_ext, supp_img_ratio):
        result = self.dimensions_validation(
            wide_image.parent, supp_img_ext, supp_img_ratio
        )
        assert isinstance(result, list)

    @pytest.mark.unit
    def test_valid_image_clannels_is_accepted(
        self, valid_rgb_image, supp_img_ext, supp_num_of_channels
    ):
        assert self.channels_validation(
            valid_rgb_image.parent, supp_img_ext, supp_num_of_channels
        )

    @pytest.mark.unit
    def test_wrong_image_channels_is_rejected(
        self, grayscale_image, supp_img_ext, supp_num_of_channels
    ):
        result = self.channels_validation(
            grayscale_image.parent, supp_img_ext, supp_num_of_channels
        )
        assert isinstance(result, list)

    @pytest.mark.unit
    def test_valid_image_dtype_is_accepted(
        self, valid_rgb_image, supp_img_ext, supp_img_dtype
    ):
        assert self.images_dtype_validation(
            valid_rgb_image.parent, supp_img_ext, supp_img_dtype
        )

    @pytest.mark.unit
    def test_wrong_image_dtype_is_rejected(
        self, wrong_dtype_of_image, supp_img_ext, supp_img_dtype
    ):
        result = self.images_dtype_validation(
            wrong_dtype_of_image.parent, supp_img_ext, supp_img_dtype
        )
        assert isinstance(result, list)

    @pytest.mark.unit
    def test_valid_image_color_format_is_accepted(
        self, valid_rgb_image, supp_img_ext, supp_color_format
    ):
        assert self.color_formats_validation(
            valid_rgb_image.parent, supp_img_ext, supp_color_format
        )

    @pytest.mark.unit
    def test_wrong_image_color_format_is_rejected(
        self, rgba_image, supp_img_ext, supp_color_format
    ):
        result = self.color_formats_validation(
            rgba_image.parent, supp_img_ext, supp_color_format
        )
        assert isinstance(result, list)
