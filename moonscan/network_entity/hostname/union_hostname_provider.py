from moonscan.network_entity.hostname.base_hostname_provider import BaseHostnameProvider


class UnionHostnameProvider(BaseHostnameProvider):
    def __init__(self, *providers: BaseHostnameProvider):
        self._providers = providers

    async def get_hostname(self, ip_address: str) -> str:
        for provider in self._providers:
            hostname = await provider.get_hostname(ip_address)
            if hostname:
                return hostname
        return ''
