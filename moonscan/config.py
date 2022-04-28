import json
from pathlib import Path
from typing import Dict

from pydantic import BaseModel


def _load_config(config_path: Path) -> Dict[str, Dict[str, str]]:
    with config_path.open('r') as file:
        return json.load(file)


class NetworkScan(BaseModel):
    network_subnet: str
    scan_interval: float


class EntityScan(BaseModel):
    ports_to_scan: int


class Config(BaseModel):
    network_scan: NetworkScan
    entity_scan: EntityScan


config = Config(**_load_config(Path('~/moonitor/scan/config.json').expanduser()))
