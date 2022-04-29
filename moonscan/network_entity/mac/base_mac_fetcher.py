from abc import ABC, abstractmethod


class BaseMacFetcher(ABC):
    @abstractmethod
    async def fetch(self, ip_address: str) -> str:
        raise NotImplementedError()
