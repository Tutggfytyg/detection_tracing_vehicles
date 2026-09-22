from pathlib import Path
from PIL import Image
from src.logger import logger


class Files_validation:
    def validate_file_extensions(
        self, data_dir: Path, supported_extentions: list[str]
    ) -> bool | list[list[str]]:
        invalid_files_and_paths = []

        for file_path in data_dir.rglob("*"):
            if not file_path.is_file():
                continue

            if file_path.suffix.lower() not in supported_extentions:
                invalid_files_and_paths.extend(
                    [file_path.suffix.lower(), str(file_path)]
                )

        if len(invalid_files_and_paths):
            return invalid_files_and_paths

        return True

    def invalid_extention_paths_logging(
        self, data_dir: Path, supported_extentions: list[str]
    ) -> None:
        ext_validation = self.validate_file_extensions(data_dir, supported_extentions)

        if type(ext_validation) != bool:
            for pairs in ext_validation:
                for file_ext, file_path in pairs:
                    logger.error(
                        "Unsupported extension: %s", file_ext, "in: %s", file_path
                    )

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

        if len(unreadable_files) == 0:
            return True

        return unreadable_files
