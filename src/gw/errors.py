class SchemaError(Exception):
    """Base class for Schema errors"""

    pass


class AlgoError(Exception):
    """Base class for errors related to Algorand"""

    pass


class DcError(Exception):
    """Base class for dataclass errors"""

    pass


class RegistryError(Exception):
    """Base class for registry errors"""

    pass
