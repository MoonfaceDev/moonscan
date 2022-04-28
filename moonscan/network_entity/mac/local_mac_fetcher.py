import uuid

from moonscan.network_entity.mac.base_mac_fetcher import BaseMacFetcher


class LocalMacFetcher(BaseMacFetcher):
    async def fetch(self, ip_address: str) -> str:
        return ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])
