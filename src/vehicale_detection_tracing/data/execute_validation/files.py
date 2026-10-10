from src.vehicale_detection_tracing.data.validation.files import Files_validation
from pathlib import Path
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path
from src.vehicale_detection_tracing.data.execute_validation.pattern import (
    Valindation_Template,
)


class Execute_Files_validation(Files_validation, Valindation_Template):
    def __init__(self, train_path: Path, test_path: Path) -> None:
        self.train_path = train_path
        self.test_path = test_path
        super().__init__()
        self.train_total = self.num_of_total_files(self.train_path)
        self.test_total = self.num_of_total_files(self.test_path)

    def execute_file_extensions_validation(
        self, train_path: Path, test_path: Path, supported_extections: list[str]
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.validate_file_extensions(train_path, supported_extections)
        test_set_res = self.validate_file_extensions(test_path, supported_extections)
        error_msg = "invalid files extention and paths"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)

    def logging_file_exetentions_validation_res(
        self, train_set_path: Path, test_set_path: Path, supported_extections: list[str]
    ) -> None:
        val_result = self.execute_file_extensions_validation(
            train_set_path, test_set_path, supported_extections
        )
        val_type = "file extention"
        self.logging_blank(val_result, val_type)

    def execute_readableness_files_validation(
        self, train_set_path: Path, test_set_path: Path
    ) -> tuple[list[str], list[str], int, int] | bool:
        train_set_res = self.readableness_files_validation(train_set_path)
        test_set_res = self.readableness_files_validation(test_set_path)
        error_msg = "unreadable files"
        return self.checking_validationing(train_set_res, test_set_res, error_msg)

    def logging_readableness_files_validation_res(
        self, train_set_path: Path, test_set_path: Path
    ) -> None:
        val_result = self.execute_readableness_files_validation(
            train_set_path, test_set_path
        )
        val_type = "files readableness"
        self.logging_blank(val_result, val_type)


if __name__ == "__main__":
    supported_extentions = [".jpg", ".csv"]
    files_val = Execute_Files_validation(train_set_path, test_set_path)
    files_val.logging_file_exetentions_validation_res(
        train_set_path, test_set_path, supported_extentions
    )
    files_val.logging_readableness_files_validation_res(train_set_path, test_set_path)
