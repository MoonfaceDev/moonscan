from nmb.NetBIOS import NetBIOS

from moonscan.network_entity.hostname.base_hostname_provider import BaseHostnameProvider


class NetBIOSHostnameProvider(BaseHostnameProvider):
    async def get_hostname(self, ip_address: str) -> str:
        netbios = NetBIOS()
        names = netbios.queryIPForName(ip_address, timeout=5)
        if names:
            return names[0]
        return ''
