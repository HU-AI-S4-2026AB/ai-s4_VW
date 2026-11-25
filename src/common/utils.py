"""Algemene hulpfuncties voor het inlezen van configuratie en opschonen van metadata."""

from pathlib import Path
from typing import Any

import pandas as pd
import yaml


def load_config(config_path: str | Path) -> dict[str, Any]:
    """
    Laadt een YAML-configuratiebestand in als dictionary.

    Parameters:
    config_path (str | Path): Pad naar het YAML-configuratiebestand.

    Returns:
    dict[str, Any]: Dictionary met configuratie-instellingen.

    Raises:
    FileNotFoundError: Als het opgegeven configuratiebestand niet bestaat.
    """
    path = Path(config_path)
    if not path.is_file():
        raise FileNotFoundError(f"Configuratiebestand niet gevonden: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data or {}


def clean_metadata(
    df: pd.DataFrame,
    existing_filenames: set[str],
) -> pd.DataFrame:
    """
    Schoont het metadatabestand (non_damage_images.xlsx) op door ontbrekende foto's
    en lege kolommen te verwijderen en kompasrichtingen boven 360 graden te corrigeren.

    Parameters:
    df (pd.DataFrame): Ruwe metadata-tabel uit non_damage_images.xlsx.
    existing_filenames (set[str]): Set met bestandsnamen die daadwerkelijk in data/raw/ staan.

    Returns:
    pd.DataFrame: Opgeschoonde metadata-tabel waarbij elke rij een bestaand beeld heeft.

    Raises:
    ValueError: Als verplichte kolommen zoals 'filename' of 'compass_angle' ontbreken.
    """
    required_cols = {"filename", "compass_angle", "latitude", "longitude"}
    if not required_cols.issubset(df.columns):
        missing = required_cols - set(df.columns)
        raise ValueError(f"Verplichte kolommen ontbreken: {missing}")

    # Verwijder kolommen die in de VolkerWessels-dataset volledig leeg zijn (PvA H8)
    cleaned = df.drop(columns=["creator", "altitude"], errors="ignore").copy()

    # Filter rijen waarvan de JPG ontbreekt op schijf (zoals image_id 1344834780613622)
    cleaned = cleaned[cleaned["filename"].isin(existing_filenames)].copy()

    # Sommige opnames hebben een compass_angle > 360 (tot 361.1); normaliseer naar [0, 360)
    cleaned["compass_angle"] = cleaned["compass_angle"] % 360.0
    return cleaned.reset_index(drop=True)
