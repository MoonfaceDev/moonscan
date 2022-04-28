import asyncio
import platform

from moonscan.network_entity.online_test.base_online_test import BaseOnlineTest


class PingOnlineTest(BaseOnlineTest):
    async def is_online(self, ip_address: str) -> bool:
        parameter = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ' '.join(['ping', parameter, '4', '-w', '4', ip_address])
        child = await asyncio.create_subprocess_shell(command,
                                                      stdout=asyncio.subprocess.DEVNULL,
                                                      stderr=asyncio.subprocess.DEVNULL)
        _, _ = await child.communicate()
        return_code = child.returncode
        return return_code == 0
