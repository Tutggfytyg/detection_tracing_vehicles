from src.vehicale_detection_tracing.data.preprocessing.annotation import (
    Annotation_Preprocessing,
)
from pathlib import Path
from src.vehicale_detection_tracing.data.execute_preprocessing.pattern import (
    Preprocessing_Pattern,
)
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path


class Execute_Annotation_Preprocessing(Annotation_Preprocessing, Preprocessing_Pattern):
    pass


if __name__ == "__main__":
    inp_supp_ext = [".csv"]
    target_format = ".txt"
    splits = {"train": train_set_path, "test": test_set_path}
    annotation_preprocessing = Execute_Annotation_Preprocessing()
    annotation_preprocessing.execute_pattern(
        splits,
        annotation_preprocessing.save_converted_to_target_format_annot_data,
        inp_supp_ext,
        target_format,
    )
