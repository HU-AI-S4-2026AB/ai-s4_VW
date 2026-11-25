"""Unittests voor kernfunctionaliteiten en dataset-edge-cases (PvA Hoofdstuk 8)."""

import numpy as np
import pandas as pd
import pytest

from src.common.utils import clean_metadata
from src.specific.task_functions import (
    crop_road_roi,
    filter_predictions,
    is_image_usable,
)


def test_clean_metadata_removes_missing_image_and_empty_columns() -> None:
    """
    Test of de ontbrekende foto (1344834780613622), lege kolommen (creator, altitude)
    en kompasrichtingen boven 360 graden correct worden verwerkt.
    """
    raw_df = pd.DataFrame({
        "filename": ["1001.jpg", "1344834780613622.jpg"],
        "image_id": [1001, 1344834780613622],
        "creator": [None, None],
        "altitude": [np.nan, np.nan],
        "latitude": [51.85, 51.86],
        "longitude": [4.35, 4.36],
        "compass_angle": [361.1, 180.0],
    })
    existing = {"1001.jpg"}

    cleaned = clean_metadata(raw_df, existing)

    assert len(cleaned) == 1
    assert cleaned.loc[0, "filename"] == "1001.jpg"
    assert "creator" not in cleaned.columns
    assert "altitude" not in cleaned.columns
    assert pytest.approx(cleaned.loc[0, "compass_angle"], rel=1e-4) == 1.1


def test_clean_metadata_raises_on_missing_required_column() -> None:
    """Test of een ValueError wordt gegooid als verplichte kolommen ontbreken."""
    invalid_df = pd.DataFrame({"filename": ["1001.jpg"]})
    with pytest.raises(ValueError):
        clean_metadata(invalid_df, {"1001.jpg"})


@pytest.mark.parametrize(
    "height,width",
    [(720, 1280), (960, 1280), (719, 1280), (533, 1280), (1120, 1280)],
)
def test_crop_road_roi_handles_multiple_resolutions(height: int, width: int) -> None:
    """Test of alle verschillende beeldformaten uit PvA H8 correct worden bijgesneden."""
    img = np.ones((height, width, 3), dtype=np.uint8)
    cropped = crop_road_roi(img, top_crop_ratio=0.20, bottom_crop_ratio=0.15)

    expected_height = int(height * 0.85) - int(height * 0.20)
    assert cropped.shape == (expected_height, width, 3)


def test_crop_road_roi_invalid_ratios_raise_error() -> None:
    """Test randgeval waarbij crop-ratio's samen >= 1.0 of negatief zijn."""
    img = np.zeros((720, 1280, 3), dtype=np.uint8)
    with pytest.raises(ValueError):
        crop_road_roi(img, top_crop_ratio=0.6, bottom_crop_ratio=0.5)
    with pytest.raises(ValueError):
        crop_road_roi(img, top_crop_ratio=-0.1, bottom_crop_ratio=0.2)


def test_is_image_usable_rejects_dark_and_empty_images() -> None:
    """Test of te donkere nachtopnames (zoals A4 dec 2020) worden afgekeurd."""
    dark_img = np.full((100, 100, 3), 5, dtype=np.uint8)
    bright_img = np.full((100, 100, 3), 120, dtype=np.uint8)
    empty_img = np.array([])

    assert is_image_usable(dark_img, min_brightness=25.0) is False
    assert is_image_usable(bright_img, min_brightness=25.0) is True
    assert is_image_usable(empty_img, min_brightness=25.0) is False


def test_filter_predictions_edge_cases() -> None:
    """Test lege detectielijst, exacte grenswaarde en ongeldige drempelwaarde."""
    preds = [
        {"bbox": [10, 10, 50, 50], "confidence": 0.35},
        {"bbox": [20, 20, 60, 60], "confidence": 0.20},
    ]
    kept = filter_predictions(preds, confidence_threshold=0.35)
    assert len(kept) == 1
    assert kept[0]["confidence"] == 0.35
    assert filter_predictions([], confidence_threshold=0.35) == []

    with pytest.raises(ValueError):
        filter_predictions(preds, confidence_threshold=1.5)
