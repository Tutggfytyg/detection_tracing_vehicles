import pytest
from src.vehicale_detection_tracing.data.validation.annotations import Annotation_validation

class Test_Annotation_Validation(Annotation_validation):

    @pytest.mark.unit
    def test_readable_annotation_is_accepted(
            self,
            valid_annotations,
            supp_annot_ext
        ):
            assert self.annotation_readableness_validation(valid_annotations.parent, supp_annot_ext)

    @pytest.mark.unit
    def test_unreadables_annotation_is_rejected(
        self,
        unreadable_annotation,
        supp_annot_ext
    ):
        result = self.annotation_readableness_validation(unreadable_annotation.parent, supp_annot_ext)
        assert isinstance(result, list)


    @pytest.mark.unit
    def test_no_missing_annotation_is_accepted(
        self,
        valid_annotations,
        supp_annot_ext,
        expected_columns
    ):
        assert self.annotation_schema_misisng_column_validation(valid_annotations.parent, supp_annot_ext, expected_columns)

    @pytest.mark.unit
    def test_missing_columns_annotation_is_rejected(
        self,
        invalid_annotation,
        supp_annot_ext,
        expected_columns
        ):
        result = self.annotation_schema_misisng_column_validation(invalid_annotation.parent, supp_annot_ext, expected_columns)
        assert isinstance(result, list)


    @pytest.mark.unit
    def test_expected_columns_annotation_is_accepted(
        self,
        valid_annotations,
        supp_annot_ext,
        expected_columns
    ):
        assert self.annotation_schema_unexpected_column_validation(valid_annotations.parent, supp_annot_ext, expected_columns)

    @pytest.mark.unit
    def test_unexpected_columns_annotation_is_rejected(
        self,
        invalid_annotation,
        supp_annot_ext,
        expected_columns
        ):
        result = self.annotation_schema_unexpected_column_validation(invalid_annotation.parent, supp_annot_ext, expected_columns)
        assert isinstance(result, list)


    @pytest.mark.unit
    def test_image_to_annotation_is_correspondent_annotation_is_accepted(
        self,
        valid_annotations,
        supp_annot_ext,
        target_column_name,
        supp_img_ext
    ):
        assert self.image_to_annotation_correspondence_validation(valid_annotations.parent, supp_annot_ext, target_column_name, supp_img_ext)

    @pytest.mark.unit
    def test_image_to_annotation_is_not_correspondence_annotation_is_rejected(
        self,
        invalid_annotation,
        supp_annot_ext,
        target_column_name,
        supp_img_ext
        ):
        result = self.image_to_annotation_correspondence_validation(invalid_annotation.parent, supp_annot_ext, target_column_name, supp_img_ext)
        assert isinstance(result, list)


    @pytest.mark.unit
    def test_valid_bbox_annotation_is_accepted(
            self,
            valid_annotations,
            supp_annot_ext
        ):
            assert self.annotataion_bbox_validation(valid_annotations.parent, supp_annot_ext)


    @pytest.mark.unit
    def test_not_valid_bbox_annotation_is_rejected(
        self,
        invalid_annotation,
        supp_annot_ext
    ):
        result = self.annotataion_bbox_validation(invalid_annotation.parent, supp_annot_ext)
        assert isinstance(result, list)


    @pytest.mark.unit
    def test_valid_classes_annotation_is_accepted(
        self,
        valid_annotations,
        supp_annot_ext,
        valid_classes
        ):
            assert self.annotation_classses_validation(valid_annotations.parent, supp_annot_ext, valid_classes)

    @pytest.mark.unit
    def test_not_valid_classes_annotation_is_rejected(
        self,
        invalid_annotation,
        supp_annot_ext,
        valid_classes
    ):
        result = self.annotation_classses_validation(invalid_annotation.parent, supp_annot_ext, valid_classes)
        assert isinstance(result, list)
