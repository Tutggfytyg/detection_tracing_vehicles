from pathlib import Path
import pandas as pd
import csv


class Annotation_validation:
    def get_annotation_paths(
        self, data_path: Path, annotation_formats: list[str]
    ) -> list[Path]:
        return [
            path
            for path in data_path.rglob("*")
            if path.is_file() and path.suffix.lower() in annotation_formats
        ]

    def total_num_of_annotations(
        self, data_path: Path, annotation_formats: list[str]
    ) -> int:
        return len(self.get_annotation_paths(data_path, annotation_formats))

    def validate_res(self, errors: list[str]) -> bool | list[str]:
        if errors:
            return errors
        else:
            return True

    def annotation_readableness_validation(
        self, data_path: Path, annotation_formats: list[str]
    ) -> list[str] | bool:

        not_readble_annotations = []
        annotation_paths = self.get_annotation_paths(data_path, annotation_formats)
        for annotation_path in annotation_paths:
            try:
                with annotation_path.open(
                    "r", encoding="utf-8-sig", newline=""
                ) as file:
                    for _ in csv.reader(file):
                        pass
            except csv.Error, UnicodeDecodeError:
                not_readble_annotations.append(annotation_path)

        return self.validate_res(not_readble_annotations)

    def annotation_schema_misisng_column_validation(
        self,
        data_path: Path,
        annotation_formats: list[str],
        expected_columns: set[str],
    ) -> list[str] | bool:
        all_missing_columns = []
        annotation_paths = self.get_annotation_paths(data_path, annotation_formats)
        for annot_path in annotation_paths:
            annonation = pd.read_csv(annot_path)
            actual_columns = set(annonation.columns)
            missing_columns_in_annot = expected_columns - actual_columns
            if len(missing_columns_in_annot) > 0:
                all_missing_columns.extend([[annot_path, missing_columns_in_annot]])

        return self.validate_res(all_missing_columns)

    def annotation_schema_unexpected_column_validation(
        self,
        data_path: Path,
        annotation_formats: list[str],
        expected_columns: set[str],
    ) -> list[str] | bool:
        all_execpected_columns = []
        annotation_paths = self.get_annotation_paths(data_path, annotation_formats)

        for annot_path in annotation_paths:
            annonation = pd.read_csv(annot_path)
            actual_columns = set(annonation.columns)
            enxected_columns_in_annot = actual_columns - expected_columns
            if len(enxected_columns_in_annot) > 0:
                all_execpected_columns.extend(
                    [[str(annot_path), str(enxected_columns_in_annot)]]
                )

        return self.validate_res(all_execpected_columns)

    def get_img_file_names(
        self, img_folder: Path, supported_images_extentions: list[str]
    ) -> list[str]:
        return [
            path.name
            for path in img_folder.iterdir()
            if path.is_file() and path.suffix.lower() in supported_images_extentions
        ]

    def get_img_file_names_from_annot(
        self, annot_file_path: Path, column_name
    ) -> list[str]:
        annotataion = pd.read_csv(annot_file_path)
        target_column = annotataion[column_name].tolist()
        return target_column

    # column name it is name of filename in annotation files
    def image_to_annotation_correspondence_validation(
        self,
        data_path: Path,
        annotation_formats: list[str],
        target_column_name,
        supported_images_extentions: list[str],
    ) -> list[str] | bool:
        not_correspondant_annotaion_to_img_pairs = []
        annotation_paths = self.get_annotation_paths(data_path, annotation_formats)
        for annotation_path in annotation_paths:
            img_dir = annotation_path.parent
            img_file_names_from_folder = self.get_img_file_names(
                img_dir, supported_images_extentions
            )

            img_file_names_from_annot = self.get_img_file_names_from_annot(
                annotation_path, target_column_name
            )
            unique_img_file_names_from_annot = set(img_file_names_from_annot)
            uniq_img_file_names_from_folder = set(img_file_names_from_folder)
            difference = (
                unique_img_file_names_from_annot ^ uniq_img_file_names_from_folder
            )
            if difference:
                difference_from_unique_img_file_names_from_annot = (
                    difference & unique_img_file_names_from_annot
                )
                difference_from_uniq_img_file_names_from_folder = (
                    difference & uniq_img_file_names_from_folder
                )
                not_correspondant_annotaion_to_img_pairs.extend(
                    [
                        [
                            str(annotation_path),
                            str(difference_from_unique_img_file_names_from_annot),
                            str(difference_from_uniq_img_file_names_from_folder),
                        ]
                    ]
                )

        return self.validate_res(not_correspondant_annotaion_to_img_pairs)

    def annotataion_bbox_validation(
        self, data_path: Path, annotation_formats: list[str]
    ):
        invalid_bboxs = []
        annotation_paths = self.get_annotation_paths(data_path, annotation_formats)
        for annotation_path in annotation_paths:
            with annotation_path.open("r", encoding="utf-8", newline="") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    try:
                        width = float(row["width"])
                        height = float(row["height"])
                        xmin = float(row["xmin"])
                        ymin = float(row["ymin"])
                        xmax = float(row["xmax"])
                        ymax = float(row["ymax"])
                        x_axis = [xmax, xmin]
                        y_axis = [ymax, ymin]
                        if not all(0 <= number <= width for number in x_axis) and not all(
                            0 <= number <= height for number in y_axis
                        ):
                            invalid_bboxs.extend([[[x_axis, y_axis], annotation_path]])
                    except KeyError:
                        invalid_bboxs.extend([["missing columns", annotation_path]])

        return self.validate_res(invalid_bboxs)

    def annotation_classses_validation(
        self,
        data_path: Path,
        annotation_formats: list[str],
        expected_classes: list[str],
    ):

        invalid_classes = []
        annotation_paths = self.get_annotation_paths(data_path, annotation_formats)

        for annotation_path in annotation_paths:
            with annotation_path.open("r", encoding="utf-8", newline="") as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    class_name = row["class"]
                    if class_name not in expected_classes:
                        invalid_classes.extend([[class_name, annotation_path]])

        return self.validate_res(invalid_classes)
