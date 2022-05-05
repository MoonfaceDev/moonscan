from abc import ABC, abstractmethod


class BaseMacProvider(ABC):
    @abstractmethod
    async def get_mac(self, ip_address: str) -> str:
        raise NotImplementedError()
