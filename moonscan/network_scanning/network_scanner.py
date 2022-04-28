import asyncio
from typing import List, Optional

from moonscan.network_entity.mac.mac_vendor_lookup import MacVendorLookup
from moonscan.network_entity.mac.simple_mac_fetcher import SimpleMacFetcher
from moonscan.network_entity.network_entity import NetworkEntity
from moonscan.network_entity.online_test.ping_online_test import PingOnlineTest
from moonscan.network_entity.ports.syn_port_scanner import SynPortScanner
from moonscan.network_scanning.base_network_scanner import BaseNetworkScanner


class NetworkScanner(BaseNetworkScanner):
    def __init__(self, ports_to_scan):
        self._online_test = PingOnlineTest()
        self._mac_fetcher = SimpleMacFetcher()
        self._mac_vendor_lookup = MacVendorLookup()
        self._port_scanner = SynPortScanner(ports_to_scan)

    async def entity_task(self, ip_address: str) -> Optional[NetworkEntity]:
        if not await self._online_test.is_online(ip_address):
            return None
        mac = await self._mac_fetcher.fetch(ip_address)
        if mac:
            vendor = await self._mac_vendor_lookup.get_vendor(mac)
        else:
            vendor = ''
        open_ports = await self._port_scanner.scan(ip_address)
        return NetworkEntity(ip=ip_address, mac=mac, vendor=vendor, open_ports=open_ports)

    async def scan(self, ip_addresses: List[str]) -> List[NetworkEntity]:
        task_results = await asyncio.gather(*[self.entity_task(ip_address) for ip_address in ip_addresses])
        return [result for result in task_results if result is not None]
