from src.vehicale_detection_tracing.data.validation.duplicates import (
    Duplicates_Validation,
)
from src.vehicale_detection_tracing.data.execute_validation.pattern import (
    Validation_Template,
)
from src.vehicale_detection_tracing.data.execute_validation.duplicates_pattern import (
    Duplicates_Validation_Template,
)
from pathlib import Path
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path


class Execute_Duplicated_Validation(
    Duplicates_Validation, Validation_Template, Duplicates_Validation_Template
):
    def __init__(
        self, train_path: Path, test_path: Path, supported_extention: str
    ) -> None:
        self.train_path = train_path
        self.test_path = test_path
        super().__init__()
        self.train_total = self.get_total_num_of_files(
            self.train_path, supported_extention
        )
        self.test_total = self.get_total_num_of_files(
            self.test_path, supported_extention
        )

    def execute_duplicates_validation(
        self, train_path: Path, test_path: Path, file_extention: str
    ) -> tuple[dict[Path, str], dict[Path, str], int, int] | bool:
        train_hash_path_pairs = self.create_hash_map(train_path, file_extention)
        test_hash_path_pairs = self.create_hash_map(test_path, file_extention)

        return self.duplicates_checking_validation(
            train_hash_path_pairs, test_hash_path_pairs
        )

    def logging_execute_duplicates_validation(
        self, train_path: Path, test_path: Path, file_extention: str, val_type: str
    ) -> None:
        val_res = self.execute_duplicates_validation(
            train_path, test_path, file_extention
        )
        self.logging_blank(val_res, val_type)


if __name__ == "__main__":
    supported_img_extention = ".jpg"
    suppotred_annot_ext = ".csv"
    img_val_type = "images duplicates"
    annot_val_type = "annotation duplicates"
    duplicates_img_val = Execute_Duplicated_Validation(
        train_set_path, test_set_path, supported_img_extention
    )
    duplicates_img_val.logging_execute_duplicates_validation(
        train_set_path, test_set_path, supported_img_extention, img_val_type
    )
    duplicates_annot_val = Execute_Duplicated_Validation(
        train_set_path, test_set_path, suppotred_annot_ext
    )
    duplicates_annot_val.logging_execute_duplicates_validation(
        train_set_path, test_set_path, suppotred_annot_ext, annot_val_type
    )
