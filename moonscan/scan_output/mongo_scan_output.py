from datetime import datetime
from typing import List

from pymongo.collection import Collection

from moonscan.network_entity.network_entity import NetworkEntity
from moonscan.scan_output.base_scan_output import BaseScanOutput


class MongoScanOutput(BaseScanOutput):
    def __init__(self, scans_collection: Collection, devices_collection: Collection):
        self._scans_collection = scans_collection
        self._devices_collection = devices_collection

    def write(self, results: List[NetworkEntity]):
        self._scans_collection.insert_one({
            'entities': [entity.dict() for entity in results],
            'scan_time': datetime.now()
        })
        for entity in results:
            self._devices_collection.update_one({
                'entity.mac': entity.mac
            }, {
                '$set': {
                    'entity': entity.dict(),
                    'scan_time': datetime.now()
                }
            }, upsert=True)
