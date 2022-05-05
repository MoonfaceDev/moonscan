import socket

from moonscan.network_entity.hostname.base_hostname_provider import BaseHostnameProvider


class SocketHostnameProvider(BaseHostnameProvider):
    async def get_hostname(self, ip_address: str) -> str:
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            return ''
