from pathlib import Path
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path
from src.vehicale_detection_tracing.data.validation.annotations import (
    Annotation_validation,
)
from src.vehicale_detection_tracing.data.execute_validation.pattern import (
    Valindation_Template,
)


class Execute_Annotations_Validation(Annotation_validation, Valindation_Template):
    def __init__(
        self, train_path: Path, test_path: Path, annotation_formats: list[str]
    ) -> None:
        self.train_path = train_path
        self.test_path = test_path
        super().__init__()
        self.train_total = self.total_num_of_annotations(
            self.train_path, annotation_formats
        )
        self.test_total = self.total_num_of_annotations(
            self.test_path, annotation_formats
        )

    def execute_annotation_readableness_validation(
        self, train_path: Path, test_path: Path, annotation_formats: list[str]
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.annotation_readableness_validation(
            train_path, annotation_formats
        )
        test_set_res = self.annotation_readableness_validation(
            test_path, annotation_formats
        )
        error_msg = "unreadable annotation"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)

    def logging_execute_annotation_readableness_validation_res(
        self, train_path: Path, test_path: Path, annotation_formats: list[str]
    ) -> None:
        val_res = self.execute_annotation_readableness_validation(
            train_path, test_path, annotation_formats
        )
        val_type = "annotation readableness"
        self.logging_blank(val_res, val_type)

    def execute_annotation_schema_misisng_column_validation(
        self,
        train_path: Path,
        test_path: Path,
        annotation_formats: list[str],
        expected_columns: set[str],
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.annotation_schema_misisng_column_validation(
            train_path, annotation_formats, expected_columns
        )
        test_set_res = self.annotation_schema_misisng_column_validation(
            test_path, annotation_formats, expected_columns
        )
        error_msg = "missing annotation column"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)

    def logging_execute_annotation_schema_misisng_column_validation_res(
        self,
        train_path: Path,
        test_path: Path,
        annotation_formats: list[str],
        expected_columns: set[str],
    ) -> None:
        val_res = self.execute_annotation_schema_misisng_column_validation(
            train_path, test_path, annotation_formats, expected_columns
        )
        val_type = "annotation columns missing"
        self.logging_blank(val_res, val_type)

    def execute_annotation_schema_unexpected_column_validation(
        self,
        train_path: Path,
        test_path: Path,
        annotation_formats: list[str],
        expected_columns: set[str],
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.annotation_schema_unexpected_column_validation(
            train_path, annotation_formats, expected_columns
        )
        test_set_res = self.annotation_schema_unexpected_column_validation(
            test_path, annotation_formats, expected_columns
        )
        error_msg = "unexpected annotation column"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)

    def logging_execute_annotation_schema_unexpected_column_validation_res(
        self,
        train_path: Path,
        test_path: Path,
        annotation_formats: list[str],
        expected_columns: set[str],
    ) -> None:
        val_res = self.execute_annotation_schema_unexpected_column_validation(
            train_path, test_path, annotation_formats, expected_columns
        )
        val_type = "unexpected annotation columns"
        self.logging_blank(val_res, val_type)

    def execute_image_to_annotation_correspondence_validation(
        self,
        train_path: Path,
        test_path: Path,
        annotation_formats: list[str],
        column_name,
        supported_images_extentions: list[str],
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.image_to_annotation_correspondence_validation(
            train_path, annotation_formats, column_name, supported_images_extentions
        )
        test_set_res = self.image_to_annotation_correspondence_validation(
            test_path, annotation_formats, column_name, supported_images_extentions
        )
        error_msg = "not correspondence annotation"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)

    def logging_execute_image_to_annotation_correspondence_validation_res(
        self,
        train_path: Path,
        test_path: Path,
        annotation_formats: list[str],
        column_name: str,
        supported_images_extentions: list[str],
    ) -> None:
        val_res = self.execute_image_to_annotation_correspondence_validation(
            train_path,
            test_path,
            annotation_formats,
            column_name,
            supported_images_extentions,
        )
        val_type = "annotation correspondence"
        self.logging_blank(val_res, val_type)

    def execute_annotataion_bbox_validation(
        self, train_path: Path, test_path: Path, annotation_formats: list[str]
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.annotataion_bbox_validation(train_path, annotation_formats)
        test_set_res = self.annotataion_bbox_validation(test_path, annotation_formats)
        error_msg = "invalid bounding box"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)

    def logging_execute_annotataion_bbox_validation_res(
        self, train_path: Path, test_path: Path, annotation_formats: list[str]
    ) -> None:
        val_res = self.execute_annotataion_bbox_validation(
            train_path, test_path, annotation_formats
        )
        val_type = "annotation bounding boxs"
        self.logging_blank(val_res, val_type)

    def execute_annotation_classses_validation(
        self,
        train_path: Path,
        test_path: Path,
        annotation_formats: list[str],
        expected_classes: list[str],
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.annotation_classses_validation(
            train_path, annotation_formats, expected_classes
        )
        test_set_res = self.annotation_classses_validation(
            test_path, annotation_formats, expected_classes
        )
        error_msg = "invalid annotaion classes"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)

    def logging_execute_annotation_classses_validation_res(
        self,
        train_path: Path,
        test_path: Path,
        annotation_formats: list[str],
        expected_classes: list[str],
    ) -> None:
        val_res = self.execute_annotation_classses_validation(
            train_path, test_path, annotation_formats, expected_classes
        )
        val_type = "annotation classes"
        self.logging_blank(val_res, val_type)


if __name__ == "__main__":
    expected_classes = ["vehicle", "ignored"]
    annotation_formats = [".csv"]
    supported_img_ext = [".jpg"]
    column_name = "filename"
    expected_columns = {
        "filename",
        "width",
        "height",
        "class",
        "xmin",
        "ymin",
        "xmax",
        "ymax",
        "confidence",
        "target_id",
    }
    annot_val = Execute_Annotations_Validation(
        train_set_path, test_set_path, annotation_formats
    )
    annot_val.logging_execute_annotation_readableness_validation_res(
        train_set_path, test_set_path, annotation_formats
    )
    annot_val.logging_execute_annotation_schema_misisng_column_validation_res(
        train_set_path, test_set_path, annotation_formats, expected_columns
    )
    annot_val.logging_execute_annotation_schema_unexpected_column_validation_res(
        train_set_path, test_set_path, annotation_formats, expected_columns
    )
    annot_val.logging_execute_image_to_annotation_correspondence_validation_res(
        train_set_path,
        test_set_path,
        annotation_formats,
        column_name,
        supported_img_ext,
    )
    annot_val.logging_execute_annotataion_bbox_validation_res(
        train_set_path, test_set_path, annotation_formats
    )
    annot_val.logging_execute_annotation_classses_validation_res(
        train_set_path, test_set_path, annotation_formats, expected_classes
    )
