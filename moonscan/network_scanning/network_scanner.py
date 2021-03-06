import asyncio
from typing import List, Optional

from moonscan.network_entity.hostname.netbios_hostname_provider import NetBIOSHostnameProvider
from moonscan.network_entity.hostname.socket_hostname_provider import SocketHostnameProvider
from moonscan.network_entity.hostname.union_hostname_provider import UnionHostnameProvider
from moonscan.network_entity.vendor.mac_vendor_provider import MacVendorProvider
from moonscan.network_entity.mac.simple_mac_provider import SimpleMacProvider
from moonscan.network_entity.network_entity import NetworkEntity
from moonscan.network_entity.online_test.ping_online_test import PingOnlineTest
from moonscan.network_entity.ports.syn_port_scanner import SynPortScanner
from moonscan.network_scanning.base_network_scanner import BaseNetworkScanner


class NetworkScanner(BaseNetworkScanner):
    def __init__(self, ports_to_scan):
        self._online_test = PingOnlineTest()
        self._hostname_provider = UnionHostnameProvider(SocketHostnameProvider(), NetBIOSHostnameProvider())
        self._mac_provider = SimpleMacProvider()
        self._mac_vendor_provider = MacVendorProvider()
        self._port_scanner = SynPortScanner(ports_to_scan)

    async def entity_task(self, ip_address: str) -> Optional[NetworkEntity]:
        if not await self._online_test.is_online(ip_address):
            return None
        hostname = await self._hostname_provider.get_hostname(ip_address)
        mac = await self._mac_provider.get_mac(ip_address)
        if mac:
            vendor = await self._mac_vendor_provider.get_vendor(mac)
        else:
            vendor = ''
        open_ports = await self._port_scanner.scan(ip_address)
        return NetworkEntity(ip=ip_address, hostname=hostname, mac=mac, vendor=vendor, open_ports=open_ports)

    async def scan(self, ip_addresses: List[str]) -> List[NetworkEntity]:
        task_results = await asyncio.gather(*[self.entity_task(ip_address) for ip_address in ip_addresses])
        return [result for result in task_results if result is not None]
