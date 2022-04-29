import asyncio
import datetime
import ipaddress

from pymongo import MongoClient

from moonscan.config import config
from moonscan.network_entity.ports.nmap_port_list_generator import NmapPortListGenerator
from moonscan.network_scanning.base_network_scanner import BaseNetworkScanner
from moonscan.network_scanning.network_scanner import NetworkScanner
from moonscan.scan_output.base_scan_output import BaseScanOutput
from moonscan.scan_output.mongo_scan_output import MongoScanOutput
from moonscan.task_scheduler import TaskScheduler


def init_scan_output() -> BaseScanOutput:
    database = MongoClient().get_database('moonlan')
    scans_collection = database.get_collection('scans')
    devices_collection = database.get_collection('devices')
    return MongoScanOutput(scans_collection, devices_collection)


def init_scanner() -> BaseNetworkScanner:
    ports_to_scan = NmapPortListGenerator().generate(config.entity_scan.ports_to_scan)
    return NetworkScanner(ports_to_scan)


def main():
    scan_output = init_scan_output()
    scanner = init_scanner()

    def scan():
        ip_addresses = [str(address) for address in ipaddress.ip_network(config.network_scan.network_subnet).hosts()]
        print(f'{datetime.datetime.now()}\tStarted scanning {len(ip_addresses)} addresses')
        entities = asyncio.run(scanner.scan(ip_addresses))
        print(f'{datetime.datetime.now()}\tScan found {len(entities)} online hosts')
        print('--- RESULTS ---')
        print(*entities, sep='\n')
        print('\n')
        scan_output.write(entities)

    task_scheduler = TaskScheduler(scan)
    task_scheduler.run(config.network_scan.scan_interval)


if __name__ == '__main__':
    main()
