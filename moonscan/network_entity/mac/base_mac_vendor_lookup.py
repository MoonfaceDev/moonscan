from abc import abstractmethod, ABC


class BaseMacVendorLookup(ABC):
    @abstractmethod
    async def get_vendor(self, mac: str) -> str:
        raise NotImplementedError()
