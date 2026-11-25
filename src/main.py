"""Startpunt (entry point) voor de bermvegetatie-detectiepipeline (ai-s4_VW)."""

import argparse
from pathlib import Path

from src.common.utils import load_config


def parse_args() -> argparse.Namespace:
    """
    Leest de command-line argumenten in voor het uitvoeren van de pipeline.

    Parameters:
    Geen.

    Returns:
    argparse.Namespace: Geparseerde CLI-argumenten (task, config, input, output).
    """
    parser = argparse.ArgumentParser(
        description="Bermvegetatie- en overgroeidetectie pipeline (VolkerWessels)"
    )
    parser.add_argument(
        "--task",
        choices=["preprocess", "train", "predict"],
        required=True,
        help="Welke stap uit de pipeline uitgevoerd moet worden.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config/config.yaml"),
        help="Pad naar het YAML-configuratiebestand.",
    )
    return parser.parse_args()


def main() -> None:
    """
    Voert de gekozen pipelinestap uit op basis van het configuratiebestand.

    Parameters:
    Geen.

    Returns:
    None.
    """
    args = parse_args()
    config = load_config(args.config)
    print(f"Start taak '{args.task}' met configuratie uit {args.config} ({len(config)} secties).")


if __name__ == "__main__":
    main()
