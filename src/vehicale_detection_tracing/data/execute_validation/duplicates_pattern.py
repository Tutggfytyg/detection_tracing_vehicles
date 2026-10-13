from pathlib import Path


class Duplicates_Validation_Template:
    def __init__(self) -> None:
        self.train_total: int = 0
        self.test_total: int = 0

    def duplicates_checking_validation(
        self, train_res, test_res
    ) -> tuple[dict[Path, str], dict[Path, str], int, int] | bool:

        duplicates_in_train = {
            key: value for key, value in train_res.items() if value in test_res.values()
        }

        duplicates_in_test = {
            key: value for key, value in test_res.items() if value in train_res.values()
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
