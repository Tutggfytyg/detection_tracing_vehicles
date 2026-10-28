from src.vehicale_detection_tracing.data.eda.images import Images_EDA
from src.vehicale_detection_tracing.data.execute_eda.pattern import EDA_Pattern
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path
from pathlib import Path


class Execute_Img_EDA(Images_EDA, EDA_Pattern):
    def execute_eda(
        self,
        splits: dict[str, Path],
        method_to_execute,
        supported_ext: list[str],
        eda_type: str,
    ):
        result = self.executig_template(splits, method_to_execute, supported_ext)
        self.logging_result(result, eda_type)


if __name__ == "__main__":
    splits = {"train": train_set_path, "test": test_set_path}
    img_EDA = Execute_Img_EDA()
    supported_img_ext = [".jpg"]

    ext_stat = img_EDA.execute_eda(
        splits,
        img_EDA.count_img_by_extentions,
        supported_img_ext,
        "extention statistic",
    )
    resolution_stat = img_EDA.execute_eda(
        splits,
        img_EDA.count_resolution_distribution,
        supported_img_ext,
        "resolution statistic",
    )
    aspect_ratio_stat = img_EDA.execute_eda(
        splits,
        img_EDA.count_aspect_ratio_disctribution,
        supported_img_ext,
        "aspect ratio statistic",
    )
    channels_stat = img_EDA.execute_eda(
        splits,
        img_EDA.count_channels_distribution,
        supported_img_ext,
        "channels statistic",
    )

    brightness_stat = img_EDA.execute_eda(
        splits,
        img_EDA.count_brightness_distribution,
        supported_img_ext,
        "brightness statistic",
    )

    contrast_stat = img_EDA.execute_eda(
        splits,
        img_EDA.count_contrast_distribution,
        supported_img_ext,
        "contrast statistic",
    )

    blur_stat = img_EDA.execute_eda(
        splits,
        img_EDA.count_blur_score_distribution,
        supported_img_ext,
        "blur statistic",
    )
