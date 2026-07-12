import json
from datetime import datetime, timedelta
from pathlib import Path


METADATA_FILE = Path(
    "data/metadata/pipeline_metadata.json"
)


def load_metadata() -> dict:
    with METADATA_FILE.open(
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def save_metadata(metadata: dict) -> None:
    with METADATA_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            metadata,
            file,
            indent=4,
        )


def get_next_date(metadata: dict) -> str:
    last_date = datetime.strptime(
        metadata["last_generated_date"],
        "%Y-%m-%d",
    )

    next_date = last_date + timedelta(days=1)

    return next_date.strftime("%Y-%m-%d")