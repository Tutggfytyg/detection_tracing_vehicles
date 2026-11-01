import pytest
import pandas as pd

@pytest.fixture
def empty_csv_annot(tmp_path):
    csv_path = tmp_path / "empty.csv"
    csv_path.write_text("", encoding="utf-8")
    return csv_path

@pytest.fixture
def valid_annotations(tmp_path) -> Path:

    path = tmp_path / "test_annotation.csv"
    data = [
        {
            "filename": "img_001.jpg",
            "class": "vahicle",
            "left": 100,
            "top": 120,
            "width": 80,
            "height": 60,
        },
        {
            "filename": "img_002.jpg",
            "class": "vahicle",
            "left": 200,
            "top": 150,
            "width": 160,
            "height": 100,
        },
    ]

    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

    return path

@pytest.fixture
def unreadable_annotation(tmp_path):
    path = tmp_path / "unreaddble_annotation.csv"

    # Write invalid binary content instead of CSV data.
    path.write_bytes(b"\x00\xff\xfe\xfa\x80\x81\x90")

    return path


@pytest.fixture
def invalid_annotation(tmp_path):
    path = tmp_path / "invalid_annotation.csv"

    data = [
        # Valid annotation
        {
            "filename": "img_001.jpg",
            "class": "car",
            "left": 100,
            "top": 120,
            "width": 80,
            "height": 60,
            "unexpected_column": "unexpected",
        },

        # Invalid class
        {
            "filename": "img_002.jpg",
            "class": "truck",
            "left": 100,
            "top": 120,
            "width": 80,
            "height": 60,
            "unexpected_column": "unexpected",
        },

        # Image does not exist
        {
            "filename": "missing_image.jpg",
            "class": "bus",
            "left": 100,
            "top": 120,
            "width": 80,
            "height": 60,
            "unexpected_column": "unexpected",
        },

        # Negative coordinates
        {
            "filename": "img_003.jpg",
            "class": "van",
            "left": -100,
            "top": 120,
            "width": 80,
            "height": 60,
            "unexpected_column": "unexpected",
        },

        # Zero bounding-box width
        {
            "filename": "img_004.jpg",
            "class": "car",
            "left": 100,
            "top": 120,
            "width": 0,
            "height": 60,
            "unexpected_column": "unexpected",
        },
    ]

    df = pd.DataFrame(data)

    # Missing required column: height
    df = df.drop(columns=["height"])

    df.to_csv(path, index=False)

    return path


@pytest.fixture
def supp_annot_ext() -> list[str]:
    return [".csv"]


@pytest.fixture
def expected_columns():
    return {
        "filename",
        "width",
        "height",
        "class",
        "xmin",
        "ymin",
        "xmax",
        "ymax",
        "confidence",
        "target_id",
    }

@pytest.fixture
def target_column_name():
    return "filename"


@pytest.fixture
def supp_img_ext() -> list[str]:
    return [".jpg", ".png"]


@pytest.fixture
def valid_classes()-> list[str]:
    return ["vehicle", "ignored"]
