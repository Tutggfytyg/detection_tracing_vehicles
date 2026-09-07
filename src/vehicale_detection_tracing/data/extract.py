from pathlib import Path
from zipfile import ZipFile


def extract_archive(archive_path: Path, output_dir: Path,) -> None:

    if not archive_path.is_file():
            raise FileNotFoundError(
                f"Archive not found: {archive_path}"
            )

    if archive_path.suffix.lower() != ".zip":
        raise ValueError(
                f"Unsupported archive format: {archive_path}"
            )

    try:
        with ZipFile(archive_path) as archive:
            if archive.testzip() is not None:
                            raise ValueError(
                                f"Corrupted ZIP archive: {archive_path}"
                            )
            for member in archive.infolist():
                target = (output_dir / member.filename).resolve()

                if not target.is_relative_to(output_dir.resolve()):
                    raise ValueError(
                        f"Unsafe archive member: {member.filename}"
                    )

            archive.extractall(output_dir)

    except BadZipFile as exc:
            raise ValueError(
                f"Invalid ZIP archive: {archive_path}"
            )  from exc


if __name__ == "__main__":
    extract_archive()
