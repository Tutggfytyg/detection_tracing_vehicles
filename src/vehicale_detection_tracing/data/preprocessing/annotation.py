from pathlib import Path
import csv


class Annotation_Preprocessing:
    def get_annot_paths(self, data_path: Path, supp_ext: list[str]) -> list[Path]:
        return [
            path
            for path in data_path.rglob("*")
            if path.is_file() and path.suffix.lower() in supp_ext
        ]

    def get_annot_data(self, data_path: Path, supp_ext: list[str]):
        annot_data = []
        annot_paths = self.get_annot_paths(data_path, supp_ext)
        annot_ext = ".csv"
        for annot_path in annot_paths:
            if annot_ext in supp_ext:
                with annot_path.open("r", newline="", encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        xmin = row["xmin"]
                        ymin = row["ymin"]
                        xmax = row["xmax"]
                        ymax = row["ymax"]
                        class_name = row["class"]
                        img_filename = row["filename"]
                        image_width = row["width"]
                        image_height = row["height"]
                        annot_info = [
                            str(annot_path),
                            img_filename,
                            class_name,
                            xmin,
                            ymin,
                            xmax,
                            ymax,
                            image_width,
                            image_height,
                        ]
                        annot_data.append(annot_info)

        return annot_data

    def annot_normalization(self, data_path: Path, supp_ext: list[str]):
        annot_stracture = self.get_annot_data(data_path, supp_ext)
        normalized_annot = []

        for (
            annot_path,
            img_filename,
            class_name,
            xmin,
            ymin,
            xmax,
            ymax,
            image_width,
            image_height,
        ) in annot_stracture:
            xmin = float(xmin)
            xmax = float(xmax)
            ymin = float(ymin)
            ymax = float(ymax)
            image_width = float(image_width)
            image_height = float(image_height)
            center_x = (xmin + xmax) / 2 / image_width
            center_y = (ymin + ymax) / 2 / image_height
            bbox_width = (xmax - xmin) / image_width
            bbox_height = (ymax - ymin) / image_height
            id = None
            if class_name == "vehicle":
                id = 0
                normalized_annot_info = [
                    str(annot_path),
                    img_filename,
                    id,
                    center_x,
                    center_y,
                    bbox_width,
                    bbox_height,
                ]
                normalized_annot.append(normalized_annot_info)

        return normalized_annot

    def change_path(
        self, old_file_path: Path, folder_name_to_change: str, new_folder_name: str
    ) -> Path:
        parts = list(old_file_path.parts)
        if folder_name_to_change in parts:
            index = parts.index(folder_name_to_change)
            parts[index] = new_folder_name
            return Path(*parts)
        else:
            raise ValueError(folder_name_to_change, " not in ", old_file_path)

    def save_converted_to_target_format_annot_data(
        self,
        data_path: Path,
        supp_inp_exts: list[str],
        target_annot_file_extention: str,
    ):
        normalized_annotation = self.annot_normalization(data_path, supp_inp_exts)

        for (
            old_annot_path,
            img_filename,
            id,
            center_x,
            center_y,
            bbox_width,
            bbox_height,
        ) in normalized_annotation:
            if target_annot_file_extention == ".txt":
                old_annot_path = Path(old_annot_path)
                new_annot_file_path = self.change_path(
                    old_annot_path, "unziped-ua-detrac", "labels"
                )
                new_annot_file_path = self.change_path(
                    new_annot_file_path, "raw", "processed"
                )
                img_filename_with_right_ext = Path(
                    Path(img_filename).stem + target_annot_file_extention
                )
                target_annot_file = Path(
                    new_annot_file_path.parent / img_filename_with_right_ext
                )
                target_annot_file.parent.mkdir(parents=True, exist_ok=True)
                if id == 0:
                    select_content = [
                        str(id),
                        str(center_x),
                        str(center_y),
                        str(bbox_width),
                        str(bbox_height),
                    ]
                    content_to_add = " ".join(select_content)

                    with target_annot_file.open("a", encoding="utf-8") as file:
                        file.write(content_to_add + "\n")
