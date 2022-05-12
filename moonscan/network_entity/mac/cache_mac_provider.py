from getmac import get_mac_address

from moonscan.network_entity.mac.base_mac_provider import BaseMacProvider

BROADCAST_MAC = '00:00:00:00:00:00'


class CacheMacProvider(BaseMacProvider):
    async def get_mac(self, ip_address: str) -> str:
        mac_address = get_mac_address(ip=ip_address) or ''
        if mac_address == BROADCAST_MAC:
            return ''
        return mac_address
