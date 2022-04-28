from abc import ABC, abstractmethod


class BaseOnlineTest(ABC):
    @abstractmethod
    async def is_online(self, ip_address: str) -> bool:
        raise NotImplementedError()
