import subprocess
import sys

modules = [
    "src.vehicale_detection_tracing.data.execute_eda.classes",
    "src.vehicale_detection_tracing.data.execute_eda.edge_cases",
    "src.vehicale_detection_tracing.data.execute_eda.images",
]

if __name__ == "__main__":
    for module in modules:
        subprocess.run(
            [sys.executable, "-m", module],
            check=True,
        )
