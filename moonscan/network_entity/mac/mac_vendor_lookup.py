from mac_vendor_lookup import AsyncMacLookup, VendorNotFoundError

from moonscan.network_entity.mac.base_mac_vendor_lookup import BaseMacVendorLookup


class MacVendorLookup(BaseMacVendorLookup):
    async def get_vendor(self, mac: str) -> str:
        try:
            return await AsyncMacLookup().lookup(mac)
        except VendorNotFoundError:
            return ''
