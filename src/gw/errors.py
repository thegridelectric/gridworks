class GwTypeError(Exception):
    """Base class for errors in making GridWorks Types"""

    pass


class BlockChainError(Exception):
    """Base class for errors related to Blockchain"""

    pass


class DcError(Exception):
    """Base class for dataclass errors"""

    pass


class RegistryError(Exception):
    """Base class for registry errors"""

    pass
