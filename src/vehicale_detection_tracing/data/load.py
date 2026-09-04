from pathlib import Path
from src.logger import logger

from huggingface_hub import snapshot_download


DATA_DIR = Path("data/raw/ua-detrac")


def load_ua_detrac() -> Path:
    dataset_path = snapshot_download(
        repo_id="abhineet123/ua_detrac",
        repo_type="dataset",
        local_dir=DATA_DIR,
    )

    return Path(dataset_path)


if __name__ == "__main__":
    path = load_ua_detrac()
    logger.info(f"Dataset: {path}")
