import argparse
from pathlib import Path

from src.vehicale_detection_tracing.data.extract import extract_archive


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract a dataset archive.")

    parser.add_argument(
        "archive",
        type=Path,
        help="Path to the dataset archive.",
    )

    parser.add_argument(
        "output",
        type=Path,
        help="Directory where the archive will be extracted.",
    )

    args = parser.parse_args()

    extract_archive(
        archive_path=args.archive,
        output_dir=args.output,
    )


if __name__ == "__main__":
    main()
