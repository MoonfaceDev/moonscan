from abc import ABC, abstractmethod


class BaseHostnameProvider(ABC):
    @abstractmethod
    async def get_hostname(self, ip_address: str) -> str:
        raise NotImplementedError()
