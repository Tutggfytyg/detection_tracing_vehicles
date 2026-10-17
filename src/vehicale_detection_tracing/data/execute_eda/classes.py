from src.vehicale_detection_tracing.data.execute_eda.pattern import EDA_Pattern
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path
from pathlib import Path
from src.vehicale_detection_tracing.data.eda.classes import Classes_EDA


class Execute_Classes_EDA(EDA_Pattern, Classes_EDA):
    def executig_template_classes(
        self,
        splits: dict[str, Path],
        method_to_execute,
        supported_ext: list[str],
        target_column: str | list[str],
    ):
        results = dict()
        for split_name, split_dir in splits.items():
            results[split_name] = method_to_execute(
                split_dir, supported_ext, target_column
            )

        return results

    def execute_eda(
        self,
        splits,
        extentions: list[str],
        method_to_exec,
        target_column: str | list[str],
        val_type: str,
    ):
        result = self.executig_template_classes(
            splits, method_to_exec, extentions, target_column
        )
        self.logging_result(result, val_type)


if __name__ == "__main__":
    classes_EDA = Execute_Classes_EDA()
    splits = {"train": train_set_path, "test": test_set_path}
    target_classes = ["vehicle"]
    supported_annot_ext = [".csv"]
    target_col = "class"

    classes_count = classes_EDA.execute_eda(
        splits,
        supported_annot_ext,
        classes_EDA.count_class_frequencies,
        target_col,
        "class frequencies",
    )
    classes_per_img = classes_EDA.execute_eda(
        splits,
        supported_annot_ext,
        classes_EDA.count_class_per_image,
        target_classes,
        "vehicles per one image",
    )
