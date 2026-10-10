from src.vehicale_detection_tracing.data.execute_validation.pattern import (
    Valindation_Template,
)
from pathlib import Path
from src.vehicale_detection_tracing.data.validation.splits import path_validate
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path


class Execute_Path_Validation(Valindation_Template):
    def __init__(self) -> None:
        super().__init__()
        self.train_total = 1  # total number of datasets
        self.test_total = 1  # total number of datasets

    def execute_path_validation(
        self, train_path: Path, test_path: Path
    ) -> bool | tuple[list[str], list[str], int, int]:
        train_res = path_validate(train_path)
        test_res = path_validate(test_path)
        error_msg = "invalid dataset path"
        return self.checking_validationing(train_res, test_res, error_msg)

    def logging_path_validation_res(self, train_path: Path, test_path: Path) -> None:
        val_result = self.execute_path_validation(train_path, test_path)
        val_type = "path splits"
        self.logging_blank(val_result, val_type)


if __name__ == "__main__":
    path_val = Execute_Path_Validation()
    path_val.logging_path_validation_res(train_set_path, test_set_path)
