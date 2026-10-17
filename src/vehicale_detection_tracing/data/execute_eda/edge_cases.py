from src.vehicale_detection_tracing.data.execute_eda.pattern import EDA_Pattern
from src.vehicale_detection_tracing.data.data_paths import train_set_path, test_set_path
from pathlib import Path
from src.vehicale_detection_tracing.data.eda.edge_cases import Edge_Case_EDA

class Execute_Edge_Casses_EDA(EDA_Pattern, Edge_Case_EDA):

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
    supported_annot_ext = [".csv"]
    edge_cases_eda = Execute_Edge_Casses_EDA()

    edge_cases_eda_bbox_ratio = edge_cases_eda.execute_eda(splits, edge_cases_eda.bounding_box, supported_annot_ext ,"bounding box ratio")
