from collections import Counter
from pathlib import Path
import pandas as pd


class Edge_Case_EDA:
    def get_annot_path(self, data_path: Path, supp_exts: list[str]):
        return [
            path
            for path in data_path.rglob("*")
            if path.is_file() and path.suffix.lower() in supp_exts
        ]

    def bounding_box(self, data_path: Path, supported_ext):
        annots_paths = self.get_annot_path(data_path, supported_ext)

        bounding_boxs_aspect_ration = Counter()

        for annot_path in annots_paths:
            annotation = pd.read_csv(annot_path)
            for _, row in annotation.iterrows():
                xmin = row["xmin"]
                ymin = row["ymin"]
                xmax = row["xmax"]
                ymax = row["ymax"]
                width = xmax - xmin
                height = ymax - ymin
                aspect_ratio = width / height
                aspect_ratio = round(aspect_ratio, 3)
                bounding_boxs_aspect_ration[aspect_ratio] += 1

        return bounding_boxs_aspect_ration
