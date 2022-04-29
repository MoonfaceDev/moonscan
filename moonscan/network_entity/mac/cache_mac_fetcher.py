from getmac import get_mac_address

from moonscan.network_entity.mac.base_mac_fetcher import BaseMacFetcher


class CacheMacFetcher(BaseMacFetcher):
    async def fetch(self, ip_address: str) -> str:
        return get_mac_address(ip=ip_address) or ''
