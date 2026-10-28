import subprocess
import sys

modules = [
    "src.vehicale_detection_tracing.data.execute_preprocessing.annotation",
    "src.vehicale_detection_tracing.data.execute_preprocessing.images",
]

if __name__ == "__main__":
    for module in modules:
        subprocess.run(
            [sys.executable, "-m", module],
            check=True,
        )
