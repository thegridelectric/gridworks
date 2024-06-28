from enum import auto
from typing import List

from gridworks.enums import GwStrEnum


class AlgoCertType(GwStrEnum):
    """
    Used to distinguish ASA vs SmartSignature certificates

    Choices and descriptions:

      * ASA: Certificate based on Algorand Standard Asset
      * SmartSig: Certificate based on Algorand Smart Signature
    """

    ASA = auto()
    SmartSig = auto()

    @classmethod
    def default(cls) -> "AlgoCertType":
        """
        Returns default value ASA
        """
        return cls.ASA

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
