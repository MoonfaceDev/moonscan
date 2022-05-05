from getmac import get_mac_address

from moonscan.network_entity.mac.base_mac_provider import BaseMacProvider


class CacheMacProvider(BaseMacProvider):
    async def get_mac(self, ip_address: str) -> str:
        return get_mac_address(ip=ip_address) or ''
