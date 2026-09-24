from pathlib import Path
from collections import Counter
import pandas as pd


class Class_distribution:
    def get_annotations(self, annotation_path: Path) -> pd.DataFrame:
        return pd.read_csv(annotation_path)

    def calculate_class_distribution(
        self, annotation_path: Path, expected_classes: list[str]
    ) -> dict[str, dict[str, float]]:
        annotations = self.get_annotations(annotation_path)
        counts = Counter(
            annotation["class"]
            for annotation in annotations
            if annotation["class"] in expected_classes
        )

        total = sum(counts.values())

        return {
            class_name: {
                "count": count,
                "percentage": count / total * 100 if total else 0.0,
            }
            for class_name, count in counts.items()
        }
