from netifaces import interfaces, ifaddresses, AF_INET

from moonscan.network_entity.mac.base_mac_provider import BaseMacProvider
from moonscan.network_entity.mac.cache_mac_provider import CacheMacProvider
from moonscan.network_entity.mac.local_mac_provider import LocalMacProvider


class SimpleMacProvider(BaseMacProvider):
    @staticmethod
    def _is_localhost(ip_address: str) -> bool:
        addresses = []
        for ifaceName in interfaces():
            addresses.extend([i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])])
        return ip_address in addresses

    def __init__(self):
        self._cache_provider = CacheMacProvider()
        self._local_provider = LocalMacProvider()

    async def get_mac(self, ip_address: str) -> str:
        if SimpleMacProvider._is_localhost(ip_address):
            return await self._local_provider.get_mac(ip_address)
        return await self._cache_provider.get_mac(ip_address)
