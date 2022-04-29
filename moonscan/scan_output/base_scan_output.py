from abc import ABC, abstractmethod
from typing import List

from moonscan.network_entity.network_entity import NetworkEntity


class BaseScanOutput(ABC):
    @abstractmethod
    def write(self, results: List[NetworkEntity]):
        raise NotImplementedError()
