from pathlib import Path
from PIL import Image


class Files_validation:
    def num_of_total_files(self, data_path: Path) -> int:
        result = 0
        for file_path in data_path.rglob("*"):
            if not file_path.is_file():
                continue
            else:
                result+=1
        return result


    def validate_file_extensions(
        self, data_dir: Path, supported_extentions: list[str]
    ) -> bool | list[list[str]]:
        invalid_files_and_paths = []

        for file_path in data_dir.rglob("*"):
            if not file_path.is_file():
                continue

            if file_path.suffix.lower() not in supported_extentions:
                invalid_files_and_paths.extend(
                    [[file_path.suffix.lower(), str(file_path)]]
                )

        if invalid_files_and_paths:
            return invalid_files_and_paths
        else:
            return True


    def readableness_files_validation(self, data_dir: Path) -> list[Path] | bool:
        unreadable_files = []

        for file_path in data_dir.rglob("*"):
            try:
                with Image.open(file_path) as image:
                    image.verify()

                # Actually decode the image data.
                with Image.open(file_path) as image:
                    image.load()

            except OSError, SyntaxError, ValueError:
                unreadable_files.append(file_path)

        if unreadable_files:
            return unreadable_files
        else:
            return True
