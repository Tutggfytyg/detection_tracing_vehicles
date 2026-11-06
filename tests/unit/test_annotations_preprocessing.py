import pytest
from src.vehicale_detection_tracing.data.preprocessing.annotation import (
    Annotation_Preprocessing,
)
import pandas as pd


class Test_Annotation_Preprocessing(Annotation_Preprocessing):
    @pytest.mark.unit
    def test_valid_annotation_with_no_missing_values_is_accepted(
        self, valid_annotations
    ):
        df = pd.read_csv(valid_annotations)
        csvfile_as_list = df.values.tolist()
        for i in csvfile_as_list:
            assert self.has_empty_values(i) == False

    @pytest.mark.unit
    def test_annotation_with_missing_values_is_rejected(self, invalid_annotation):
        result = []
        df = pd.read_csv(invalid_annotation)
        csvfile_as_list = df.values.tolist()
        for i in csvfile_as_list:
            result.append(self.has_empty_values(i))
        assert any(result)

    @pytest.mark.unit
    def test_if_annotation_normalization_can_be_executed_is_accepted(
        self, valid_annotations, supp_annot_ext
    ):
        result = self.annot_normalization(valid_annotations.parent, supp_annot_ext)
        assert result != None

    @pytest.mark.unit
    def test_if_annotation_normalization_can_not_be_executed_is_rejected(
        self, invalid_annotation, supp_annot_ext
    ):
        result = self.annot_normalization(invalid_annotation.parent, supp_annot_ext)
        assert result == None

    @pytest.mark.unit
    def test_if_annotation_get_data_can_be_executed_is_accepted(
        self, valid_annotations, supp_annot_ext
    ):
        result = self.get_annot_data(valid_annotations.parent, supp_annot_ext)
        assert result != None

    @pytest.mark.unit
    def test_if_annotation_get_data_can_not_be_executed_is_rejected(
        self, invalid_annotation, supp_annot_ext
    ):
        result = self.get_annot_data(invalid_annotation.parent, supp_annot_ext)
        assert result == None

    @pytest.mark.unit
    def test_if_annotation_data_cleaning_can_be_executed_is_accepted(
        self, valid_annotations, supp_annot_ext
    ):
        result = self.data_cleaning(valid_annotations.parent, supp_annot_ext)
        assert result != None

    @pytest.mark.unit
    def test_if_annotation_data_cleaning_can_not_be_executed_is_rejected(
        self, invalid_annotation, supp_annot_ext
    ):
        result = self.data_cleaning(invalid_annotation.parent, supp_annot_ext)
        assert result == None

    @pytest.mark.unit
    def test_if_annotation_data_converting_can_be_executed_is_accepted(
        self, valid_annotations, supp_annot_ext, target_converted_annotation_ext
    ):
        result = self.save_converted_to_target_format_annot_data(
            valid_annotations.parent, supp_annot_ext, target_converted_annotation_ext
        )
        assert result != False

    @pytest.mark.unit
    def test_if_annotation_data_converting_can_not_be_executed_is_rejected(
        self, invalid_annotation, supp_annot_ext, target_converted_annotation_ext
    ):
        result = self.save_converted_to_target_format_annot_data(
            invalid_annotation.parent, supp_annot_ext, target_converted_annotation_ext
        )
        assert result == False
