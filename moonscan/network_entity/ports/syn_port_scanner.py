import asyncio
from typing import List

from moonscan.network_entity.ports.base_port_scanner import BasePortScanner


class SynPortScanner(BasePortScanner):
    def __init__(self, ports_to_scan: List[int], *options: str):
        self._ports_to_scan = ports_to_scan
        self._options = options

    async def scan(self, ip_address: str) -> List[int]:
        async def scan_port_task(port: int) -> bool:
            try:
                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection(ip_address, port),
                    timeout=2
                )
                writer.close()
                await writer.wait_closed()
                return True
            except (ConnectionRefusedError, asyncio.TimeoutError, OSError):
                return False

        tasks = (scan_port_task(port) for port in self._ports_to_scan)
        port_states = await asyncio.gather(*tasks)
        return [self._ports_to_scan[index] for index in range(len(self._ports_to_scan)) if port_states[index]]
