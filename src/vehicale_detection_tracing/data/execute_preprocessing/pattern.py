from pathlib import Path


class Preprocessing_Pattern:
    def exeute_pattern(
        self,
        splits: dict[str, Path],
        method_to_execute,
        supported_ext: list[str],
        target_annot_file_extention: str,
    ) -> None:
        for split_name, split_dir in splits.items():
            method_to_execute(split_dir, supported_ext, target_annot_file_extention)
