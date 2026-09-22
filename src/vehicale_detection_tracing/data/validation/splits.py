from pathlib import Path


def path_validate(path: Path) -> bool:
    return path.is_dir()
