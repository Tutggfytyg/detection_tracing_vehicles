from pathlib import Path


class Files_validation:
    def num_of_total_files(self, data_path: Path) -> int:
        return len(self.get_files_paths(data_path))

    def get_files_paths(self, data_path: Path) -> list[Path]:
        return [path for path in data_path.rglob("*") if path.is_file()]

    def validate_file_extensions(
        self, data_path: Path, supported_extentions: list[str]
    ) -> bool | list[str]:
        invalid_files_and_paths = []
        files_paths = self.get_files_paths(data_path)

        for file_path in files_paths:
            if file_path.suffix.lower() not in supported_extentions:
                invalid_files_and_paths.extend(
                    [[file_path.suffix.lower(), str(file_path)]]
                )

        if invalid_files_and_paths:
            return invalid_files_and_paths
        else:
            return True

    def readableness_files_validation(self, data_path: Path) -> list[str] | bool:
        unreadable_files = []
        files_paths = self.get_files_paths(data_path)

        for file_path in files_paths:
            try:
                with file_path.open("rb") as file:
                    file.read(1)

            except OSError, ValueError:
                unreadable_files.append(str(file_path))

        if unreadable_files:
            return unreadable_files
        else:
            return True
