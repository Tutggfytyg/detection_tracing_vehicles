import subprocess
import sys

modules = [
    "src.vehicale_detection_tracing.data.execute_validation.paths",
    "src.vehicale_detection_tracing.data.execute_validation.files",
    "src.vehicale_detection_tracing.data.execute_validation.annotations",
    "src.vehicale_detection_tracing.data.execute_validation.duplicates",
    "src.vehicale_detection_tracing.data.execute_validation.images",
]

if __name__ == "__main__":
    for module in modules:
        subprocess.run(
            [sys.executable, "-m", module],
            check=True,
        )
