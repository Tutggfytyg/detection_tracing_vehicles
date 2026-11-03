from src.vehicale_detection_tracing.data.validation.files import Files_validation
import pytest


class Test_Files_Validation(Files_validation):
    @pytest.mark.unit
    def test_valid_file_extention_is_accepted(
        self, valid_annotations_file, valid_image, supp_files_ext
    ):
        assert self.validate_file_extensions(
            valid_annotations_file.parent, supp_files_ext
        )
        assert self.validate_file_extensions(valid_image, supp_files_ext)

    @pytest.mark.unit
    def test_not_valid_file_extention_is_rejected(
        self, unsupp_file_ext, supp_files_ext
    ):
        result = self.validate_file_extensions(unsupp_file_ext.parent, supp_files_ext)
        assert isinstance(result, list)

    @pytest.mark.unit
    def test_readable_file_is_accepted(self, valid_annotations_file, valid_image):
        assert self.readableness_files_validation(valid_annotations_file.parent)
        assert self.readableness_files_validation(valid_image)

    @pytest.mark.unit
    def test_not_readable_file_is_rejected(self, unreadable_file):
        result = self.readableness_files_validation(unreadable_file.parent)
        assert isinstance(result, list)
