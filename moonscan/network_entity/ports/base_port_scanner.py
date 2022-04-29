from abc import ABC, abstractmethod
from typing import List


class BasePortScanner(ABC):
    @abstractmethod
    async def scan(self, ip_address: str) -> List[int]:
        raise NotImplementedError()
