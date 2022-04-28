from netifaces import interfaces, ifaddresses, AF_INET

from moonscan.network_entity.mac.base_mac_fetcher import BaseMacFetcher
from moonscan.network_entity.mac.cache_mac_fetcher import CacheMacFetcher
from moonscan.network_entity.mac.local_mac_fetcher import LocalMacFetcher


class SimpleMacFetcher(BaseMacFetcher):
    @staticmethod
    def _is_localhost(ip_address: str) -> bool:
        addresses = []
        for ifaceName in interfaces():
            addresses.extend([i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])])
        return ip_address in addresses

    def __init__(self):
        self._cache_fetcher = CacheMacFetcher()
        self._local_fetcher = LocalMacFetcher()

    async def fetch(self, ip_address: str) -> str:
        if SimpleMacFetcher._is_localhost(ip_address):
            return await self._local_fetcher.fetch(ip_address)
        return await self._cache_fetcher.fetch(ip_address)
