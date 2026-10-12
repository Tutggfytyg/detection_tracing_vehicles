from src.vehicale_detection_tracing.data.validation.duplicates import (
    Duplicates_Validation,
)
from src.vehicale_detection_tracing.data.execute_validation.pattern import (
    Validation_Template,
)
from pathlib import Path
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path


class Execute_Duplicated_Validation(Duplicates_Validation, Validation_Template):
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
        train_hash_path_pair = self.create_hash_map(train_path, file_extention)
        test_hash_path_pair = self.create_hash_map(test_path, file_extention)

        duplicates_in_train = {
            key: value
            for key, value in train_hash_path_pair.items()
            if value in test_hash_path_pair.values()
        }

        duplicates_in_test = {
            key: value
            for key, value in test_hash_path_pair.items()
            if value in train_hash_path_pair.values()
        }
        num_of_train_duplicates = len(duplicates_in_train)
        num_of_test_duplicates = len(duplicates_in_test)
        result = (
            duplicates_in_train,
            duplicates_in_test,
            num_of_train_duplicates,
            num_of_test_duplicates,
        )

        if duplicates_in_train or duplicates_in_test:
            return result
        else:
            return True

    def logging_execute_duplicates_validation(
        self, train_path: Path, test_path: Path, file_extention: str
    ) -> None:
        val_res = self.execute_duplicates_validation(
            train_path, test_path, file_extention
        )
        val_type = "duplicates"
        self.logging_blank(val_res, val_type)


if __name__ == "__main__":
    supported_extention = ".jpg"
    duplicates_val = Execute_Duplicated_Validation(
        train_set_path, test_set_path, supported_extention
    )
    duplicates_val.logging_execute_duplicates_validation(
        train_set_path, test_set_path, supported_extention
    )
