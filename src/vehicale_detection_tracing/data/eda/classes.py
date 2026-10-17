from pathlib import Path
from collections import Counter
import pandas as pd


class Classes_EDA:
    def get_annotations_paths(
        self, data_path: Path, supp_exts: list[str]
    ) -> list[Path]:
        return [
            path
            for path in data_path.rglob("*")
            if path.is_file() and path.suffix.lower() in supp_exts
        ]

    def count_class_frequencies(
        self, data_path: Path, extentions: list[str], classes_column: str
    ) -> dict[str, int]:

        annotation_paths = self.get_annotations_paths(data_path, extentions)
        class_counts = Counter()

        for annotation_path in annotation_paths:
            annot = pd.read_csv(annotation_path)

            for value in annot[classes_column]:
                class_counts[value] += 1

        return dict(class_counts)

    def count_class_per_image(
        self, data_path: Path, extentions: list[str], target_classes: list[str]
    ):
        annot_paths = self.get_annotations_paths(data_path, extentions)
        class_per_img = Counter()
        filename_col = "filename"

        for annot_path in annot_paths:
            annot = pd.read_csv(annot_path)

            df = annot[annot["class"].isin(target_classes)]

            counts = df.groupby(filename_col).size()

            for file_name, count in counts.items():
                image_key = f"{annot_path}:{file_name}"
                class_per_img[image_key] = int(count)

        distribution = Counter(class_per_img.values())

        return distribution
