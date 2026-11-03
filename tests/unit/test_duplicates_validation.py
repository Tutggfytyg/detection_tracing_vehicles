import pytest
from src.vehicale_detection_tracing.data.validation.duplicates import (
    Duplicates_Validation,
)
from src.vehicale_detection_tracing.data.execute_validation.duplicates_pattern import (
    Duplicates_Validation_Template,
)


class Test_Duplicates_Validation(Duplicates_Validation):
    @pytest.mark.unit
    def test_no_duplicactes_is_accepted(self, jpg_image, jpg_image1):
        file_h_m = self.calculate_file_hash(jpg_image)
        file1_h_m = self.calculate_file_hash(jpg_image1)
        assert file_h_m != file1_h_m

    @pytest.mark.unit
    def test_dupliactes_is_rejected(self, annotation_file):
        file_h_m = self.calculate_file_hash(annotation_file)
        file1_h_m = self.calculate_file_hash(annotation_file)
        assert file_h_m == file1_h_m
