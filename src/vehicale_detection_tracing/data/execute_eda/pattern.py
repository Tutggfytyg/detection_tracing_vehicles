from src.logger import logger
from pathlib import Path


class EDA_Pattern:
    def executig_template(
        self, splits: dict[str, Path], method_to_execute, supported_ext: list[str]
    ):
        results = dict()
        for split_name, split_dir in splits.items():
            results[split_name] = method_to_execute(split_dir, supported_ext)

        return results

    def logging_result(self, eda_method_result, eda_type: str) -> None:
        logger.info("%s , %s", eda_type, eda_method_result)
