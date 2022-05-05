from typing import List

from pydantic import BaseModel


class NetworkEntity(BaseModel):
    ip: str
    hostname: str
    mac: str
    vendor: str
    open_ports: List[int]
