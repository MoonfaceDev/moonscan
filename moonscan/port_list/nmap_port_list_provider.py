import re
from pathlib import Path
from typing import List

from moonscan.port_list.base_port_list_provider import BasePortListProvider
from moonscan.network_entity.ports.exceptions import PortNumberOverflowError, PortsFileNotFoundError, \
    BadPortsFileError


class NmapPortListProvider(BasePortListProvider):
    def __init__(self, path: Path = Path('/usr/share/nmap/nmap-services')):
        self._path = path

    def get_list(self, number_of_ports: int) -> List[int]:
        if not self._path.is_file():
            raise PortsFileNotFoundError()
        with self._path.open('r') as file:
            lines = file.readlines()
        if number_of_ports > len(lines):
            raise PortNumberOverflowError()
        try:
            lines = lines[22:]
            table = [re.split('\t', line) for line in lines]
            table = list(filter(lambda line: 'tcp' in line[1], table))
            table = sorted(table, reverse=True, key=lambda line: line[2])
            return [int(re.split('/', line[1])[0]) for line in table[:number_of_ports]]
        except (IndexError, ValueError):
            raise BadPortsFileError()
