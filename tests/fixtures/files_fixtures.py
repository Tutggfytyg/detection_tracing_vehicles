import pytest
from PIL import Image
import pandas as pd


@pytest.fixture
def valid_image(tmp_path):
    image_path = tmp_path / "valid_rgb.jpg"

    image = Image.new("RGB", (100, 100), color=(0, 0, 0))
    image.save(image_path, format="JPEG")

    return image_path


@pytest.fixture
def valid_annotations_file(tmp_path):

    path = tmp_path / "test_annotation.csv"
    data = [
        {
            "filename": "img_001.jpg",
            "class": "vahicle",
            "left": 100,
            "top": 120,
            "width": 80,
            "height": 60,
        }
    ]

    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

    return path


@pytest.fixture
def supp_files_ext() -> list[str]:
    return [".jpg", ".png", ".csv"]


@pytest.fixture
def unsupp_file_ext(tmp_path):
    path = tmp_path / "gif_file.gif"

    image = Image.new(
        "RGB",
        (100, 100),
        color="red",
    )

    image.save(path, format="GIF")

    return path


@pytest.fixture
def unreadable_file(tmp_path):
    path = tmp_path / "unreadble.csv"

    path.write_bytes(b"\xff\xfe\xfa\x80\x81\x90\xff")
    path.chmod(0o000)

    return path
