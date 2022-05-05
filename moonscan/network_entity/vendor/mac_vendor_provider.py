from mac_vendor_lookup import AsyncMacLookup, VendorNotFoundError

from moonscan.network_entity.vendor.base_mac_vendor_provider import BaseMacVendorProvider


class MacVendorProvider(BaseMacVendorProvider):
    async def get_vendor(self, mac: str) -> str:
        try:
            return await AsyncMacLookup().lookup(mac)
        except VendorNotFoundError:
            return ''
