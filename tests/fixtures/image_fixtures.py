import pytest
from PIL import Image
import numpy as np


@pytest.fixture
def valid_rgb_image(tmp_path):
    image_path = tmp_path / "valid_rgb.jpg"

    image = Image.new("RGB", (100, 100), color=(0, 0, 0))
    image.save(image_path, format="JPEG")

    return image_path


@pytest.fixture
def wrong_dtype_of_image(tmp_path) -> np.ndarray:
    path = tmp_path / "wrong_dtype_of_image.png"
    image_array = np.random.randint(
        0,
        65536,
        size=(480, 640),
        dtype=np.uint16,
    )

    image = Image.fromarray(image_array)
    image.save(path, format="PNG")

    return path


@pytest.fixture
def grayscale_image(tmp_path):
    path = tmp_path / "grayscale.png"
    Image.new("L", (640, 640), color=128).save(path)
    return path


@pytest.fixture
def wide_image(tmp_path):
    path = tmp_path / "wide.jpg"
    Image.new("RGB", (1000, 100), color="red").save(path)
    return path


@pytest.fixture
def corrupt_image(tmp_path):
    path = tmp_path / "corrupt.jpg"
    path.write_bytes(b"invalid image")
    return path


@pytest.fixture
def empty_file(tmp_path):
    path = tmp_path / "empty.jpg"
    path.touch()
    return path


@pytest.fixture
def rgba_image(tmp_path):
    image_path = tmp_path / "rgba_image.png"

    image = Image.new("RGBA", (100, 100), color=(255, 0, 0, 0))
    image.save(image_path, format="PNG")

    return image_path


@pytest.fixture
def supp_img_ext() -> list[str]:
    return [".jpg", ".png"]


@pytest.fixture
def supp_img_ratio() -> float:
    return 1.0


@pytest.fixture
def supp_num_of_channels() -> int:
    return 3


@pytest.fixture
def supp_img_dtype() -> np.dtype:
    return np.uint8


@pytest.fixture
def supp_color_format() -> str:
    return "RGB"
