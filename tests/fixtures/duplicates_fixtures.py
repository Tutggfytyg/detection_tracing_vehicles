import pytest
import pandas as pd
from PIL import Image


@pytest.fixture
def annotation_file(tmp_path):

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
def annotation_file1(tmp_path1):

    path = tmp_path / "test_annotation1.csv"
    data = [
        {
            "filename": "img_002.jpg",
            "class": "vahicle",
            "left": 200,
            "top": 130,
            "width": 70,
            "height": 50,
        }
    ]

    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

    return path


@pytest.fixture
def jpg_image(tmp_path):
    image_path = tmp_path / "valid_rgb.jpg"

    image = Image.new("RGB", (100, 100), color=(0, 0, 0))
    image.save(image_path, format="JPEG")

    return image_path


@pytest.fixture
def jpg_image1(tmp_path):
    image_path = tmp_path / "valid_rgb1.jpg"

    image = Image.new("RGB", (120, 120), color=(40, 0, 0))
    image.save(image_path, format="JPEG")

    return image_path
