from pathlib import Path
from hashlib import sha256


class Duplicates_validation:
    def calculate_file_hash(self, file_path: Path) -> str:
        hasher = sha256()

        with file_path.open("rb") as file:
            for chunk in iter(lambda: file.read(8192), b""):
                hasher.update(chunk)

        return hasher.hexdigest()

    def create_hash_map(self, file_dir: Path, file_extention: type) -> dict[str, Path]:
        hash_map = {}

        for file_path in file_dir.rglob(f"*.{file_extention}"):
            file_hash = self.calculate_file_hash(file_path)
            hash_map[file_hash] = file_path

        return hash_map
