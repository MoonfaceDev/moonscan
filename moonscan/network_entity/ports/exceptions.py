class PortScanError(Exception):
    pass


class PortsFileNotFoundError(PortScanError):
    pass


class PortNumberOverflowError(PortScanError):
    pass


class BadPortsFileError(PortScanError):
    pass
