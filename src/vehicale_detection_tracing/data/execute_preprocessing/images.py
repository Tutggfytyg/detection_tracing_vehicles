from pathlib import Path
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path
from src.vehicale_detection_tracing.data.preprocessing.images import (
    Images_Preprocessing,
)


class Execute_Images_Preprocessing(Images_Preprocessing):
    def execute_pattern(
        self,
        splits: dict[str, Path],
        method_to_execute,
        supported_ext: list[str],
    ) -> None:
        for split_name, split_dir in splits.items():
            method_to_execute(split_dir, supported_ext)


if __name__ == "__main__":
    splits = {"train": train_set_path, "test": test_set_path}
    supported_ext = [".jpg"]
    execute_img_preprecossing = Execute_Images_Preprocessing()
    execute_img_preprecossing.execute_pattern(
        splits, execute_img_preprecossing.copy_images, supported_ext
    )
