from pathlib import Path
from hashlib import sha256


class Duplicates_Validation:
    def get_file_paths(self, data_path: Path, supported_expention: str) -> list[Path]:
        return [
            path
            for path in data_path.rglob(f"*{supported_expention}")
            if path.is_file() and path.suffix.lower()
        ]

    def get_total_num_of_files(self, data_path: Path, supported_expention: str) -> int:
        return len(self.get_file_paths(data_path, supported_expention))

    def calculate_file_hash(self, file_path: Path) -> str:
        hasher = sha256()

        with file_path.open("rb") as file:
            for chunk in iter(lambda: file.read(8192), b""):
                hasher.update(chunk)

        return hasher.hexdigest()

    def create_hash_map(self, data_path: Path, file_extention: str) -> dict[Path, str]:
        hash_map = {}
        files_paths = self.get_file_paths(data_path, file_extention)
        for file_path in files_paths:
            file_hash = self.calculate_file_hash(file_path)
            hash_map[file_path] = file_hash

        return hash_map
