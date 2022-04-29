from abc import abstractmethod, ABC
from typing import List

from moonscan.network_entity.network_entity import NetworkEntity


class BaseNetworkScanner(ABC):
    @abstractmethod
    async def scan(self, ip_addresses: List[str]) -> List[NetworkEntity]:
        """
        :param ip_addresses: IP addresses to check
        :return: NetworkEntities of existing IP addresses
        """
        raise NotImplementedError()
