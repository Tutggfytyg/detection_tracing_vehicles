from pathlib import Path
import pandas as pd
from src.logger import logger
import math


class Annotation_validation:
    def annotation_existence_validation(
        self, images_dir: Path, annotation_dir: Path, anotation_format: str
    ) -> list[Path] | bool:

        missing_annotations = []

        for image_path in images_dir.rglob("*"):
            if not image_path.is_file():
                continue

            relative_path = image_path.relative_to(images_dir)

            annotation_path = annotation_dir / relative_path.with_suffix(
                anotation_format
            )

            if not annotation_path.is_file():
                missing_annotations.append(image_path)

        if len(missing_annotations) == 0:
            return True
        return missing_annotations

    def annoantion_empty_validation(
        self,
        annonation_extention: str,
        annotation_dir: Path,
    ) -> list[Path] | bool:
        empty_files = []

        for annotation_path in annotation_dir.rglob(f"*.{annonation_extention}"):
            df = pd.DataFrame
            try:
                df = pd.read_csv(annotation_path)
            except OSError, pd.errors.EmptyDataError, pd.errors.ParserError:
                empty_files.append(annotation_path)

            if df.empty:
                empty_files.append(annotation_path)

        if len(empty_files) == 0:
            return True
        return empty_files

    def annotation_columns_validation(
        self, annotation_path: Path, expected_columns: list[str]
    ) -> bool:
        try:
            df = pd.read_csv(annotation_path)
        except OSError, pd.errors.EmptyDataError, pd.errors.ParserError:
            return False

        if len(df.columns) != len(expected_columns):
            logger.error(
                "Invalid number of annotation fields in %s: expected %d, got %d",
                annotation_path,
                len(expected_columns),
                len(df.columns),
            )
            return False

        if set(df.columns) != expected_columns:
            logger.error(
                "Invalid annotation fields in %s: %s",
                annotation_path,
                list(df.columns),
            )
            return False

        return True

    def invalid_class_ids_validation(
        self,
        annotation_path: Path,
        allowed_class_ids: set[int],
    ) -> list[int] | bool:
        invalid_class_ids = []

        df = pd.read_csv(annotation_path)

        for class_id in df["class_id"]:
            if pd.isna(class_id):
                invalid_class_ids.append(class_id)
                continue

            if int(class_id) not in allowed_class_ids:
                invalid_class_ids.append(int(class_id))

        if len(invalid_class_ids) == 0:
            return True
        return invalid_class_ids

    def coordinates_of_image_validation(
        self,
        annotation_path: Path,
        image_width: int,
        image_height: int,
    ) -> list[tuple[int, str]] | bool:
        df = pd.read_csv(annotation_path)

        invalid = []

        for row_number, row in df.iterrows():
            csv_row = row_number + 2

            try:
                x = float(row["x"])
                y = float(row["y"])
                width = float(row["width"])
                height = float(row["height"])
            except TypeError, ValueError:
                invalid.append((csv_row, "coordinates are not numeric"))
                continue

            coordinates = (x, y, width, height)

            if not all(math.isfinite(value) for value in coordinates):
                invalid.append((csv_row, "coordinates contain NaN or infinity"))
                continue

            if x < 0 or y < 0:
                invalid.append((csv_row, "x or y is negative"))
                continue

            if width <= 0 or height <= 0:
                invalid.append((csv_row, "width or height is not positive"))
                continue

            right = x + width
            bottom = y + height

            if right > image_width or bottom > image_height:
                invalid.append((csv_row, "bounding box extends outside image"))

        if len(invalid) == 0:
            return True
        return invalid
