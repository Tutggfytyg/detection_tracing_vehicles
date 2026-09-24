from pathlib import Path


class Data__leakage_validation:
    def get_split_data(self, target_dir: Path) -> set[str]:
        target_sequences = {
            path.parent.name for path in target_dir.rglob("*") if path.is_file()
        }
        return target_sequences

    def data_leakage_validation(
        self,
        train_dir: Path,
        test_dir: Path,
    ) -> set[str] | bool:
        train_sequences = self.get_split_data(train_dir)
        test_sequences = self.get_split_data(test_dir)

        leakage = train_sequences & test_sequences
        if len(leakage) == 0:
            return True

        return leakage
