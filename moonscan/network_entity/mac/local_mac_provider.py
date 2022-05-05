import uuid

from moonscan.network_entity.mac.base_mac_provider import BaseMacProvider


class LocalMacProvider(BaseMacProvider):
    async def get_mac(self, ip_address: str) -> str:
        return ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])
