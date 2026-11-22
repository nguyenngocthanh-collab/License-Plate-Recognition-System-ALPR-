from dataclasses import dataclass
from typing import TypeAlias
import numpy as np

Image: TypeAlias = np.ndarray


@dataclass
class Detection:
    bbox: tuple[int, int, int, int]
    confidence: float


def detect_plates(image: Image) -> list[Detection]:
    """
    Detect license plates in an image.

    Args:
        image: Original image in BGR format (H, W, 3).

    Returns:
        A list of detected license plates.
    """
    ...