"""Projectspecifieke functies voor beeldvoorbereiding, filtering en locatiekoppeling."""

from typing import Any

import numpy as np


def crop_road_roi(
    image: np.ndarray,
    top_crop_ratio: float,
    bottom_crop_ratio: float,
) -> np.ndarray:
    """
    Snijdt de lucht (bovenkant) en de motorkap/statusbalk (onderkant) weg uit een dashcambeeld.

    Parameters:
    image (np.ndarray): Inputafbeelding als NumPy-array met vorm (H, W, C) of (H, W).
    top_crop_ratio (float): Fractie van de bovenkant die wordt weggesneden (0.0 tot 1.0).
    bottom_crop_ratio (float): Fractie van de onderkant die wordt weggesneden (0.0 tot 1.0).

    Returns:
    np.ndarray: De bijgesneden afbeelding (Region of Interest).

    Raises:
    ValueError: Als de afbeelding leeg is of de crop-ratio's ongeldig zijn.
    """
    if image.size == 0 or image.ndim < 2:
        raise ValueError("Inputafbeelding moet minimaal 2 dimensies hebben en niet leeg zijn.")
    if top_crop_ratio < 0 or bottom_crop_ratio < 0 or (top_crop_ratio + bottom_crop_ratio) >= 1.0:
        raise ValueError("Ongeldige crop-ratio's: som moet kleiner zijn dan 1.0 en niet-negatief.")

    height = image.shape[0]
    start_y = int(height * top_crop_ratio)
    # Onderkant bevat in de VolkerWessels-set de motorkap (PvA H8); fractie komt uit config.yaml
    end_y = int(height * (1.0 - bottom_crop_ratio))
    return image[start_y:end_y, :]


def is_image_usable(image: np.ndarray, min_brightness: float) -> bool:
    """
    Controleert of een straatbeeld niet te donker is om de berm te kunnen beoordelen.

    Parameters:
    image (np.ndarray): Inputafbeelding als NumPy-array.
    min_brightness (float): Minimale gemiddelde pixelintensiteit (0-255).

    Returns:
    bool: True als het beeld helder genoeg is, anders False.
    """
    if image.size == 0:
        return False
    return float(np.mean(image)) >= min_brightness


def filter_predictions(
    predictions: list[dict[str, Any]],
    confidence_threshold: float,
) -> list[dict[str, Any]]:
    """
    Filtert modelvoorspellingen op basis van de gekozen confidence-threshold.

    Parameters:
    predictions (list[dict[str, Any]]): Lijst met detecties (elk met sleutel 'confidence').
    confidence_threshold (float): Minimale betrouwbaarheidsscore tussen 0.0 en 1.0.

    Returns:
    list[dict[str, Any]]: Gefilterde lijst met detecties op of boven de drempelwaarde.

    Raises:
    ValueError: Als confidence_threshold buiten het bereik [0.0, 1.0] ligt.
    """
    if not 0.0 <= confidence_threshold <= 1.0:
        raise ValueError("confidence_threshold moet tussen 0.0 en 1.0 liggen.")

    return [
        pred for pred in predictions
        if float(pred.get("confidence", 0.0)) >= confidence_threshold
    ]
