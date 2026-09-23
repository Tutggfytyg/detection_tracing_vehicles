import pandas as pd
from pathlib import Path


class Classes_valiadation:
    def classes_validaiton(
        self, annotation_path: Path, allowed_classes: set[str]
    ) -> set[str] | bool:
        df = pd.read_csv(annotation_path)

        invalid_classes = set(df["class"].dropna()) - allowed_classes

        if len(invalid_classes) == 0:
            return True
        return invalid_classes
