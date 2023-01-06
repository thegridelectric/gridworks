"""Type initial.tadeed.algo.transfer, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gridworks.errors import SchemaError


def check_is_algo_address_string_format(v: str) -> None:
    """
    AlgoAddressStringFormat format: The public key of a private/public Ed25519
    key pair, transformed into an  Algorand address, by adding a 4-byte checksum
    to the end of the public key and then encoding in base32.

    Raises:
        ValueError: if not AlgoAddressStringFormat format
    """
    import algosdk

    at = algosdk.abi.AddressType()
    try:
        result = at.decode(at.encode(v))
    except Exception as e:
        raise ValueError(f"Not AlgoAddressStringFormat: {e}")


def check_is_algo_msg_pack_encoded(v: str) -> None:
    """
    AlgoMSgPackEncoded format: the format of an  transaction sent to
    the Algorand blockchain.

    Raises:
        ValueError: if not AlgoMSgPackEncoded  format
    """
    import algosdk

    try:
        algosdk.encoding.future_msgpack_decode(v)
    except Exception as e:
        raise ValueError(f"Not AlgoMsgPackEncoded format: {e}")


class InitialTadeedAlgoTransfer(BaseModel):
    """TaValidator sends to GNodeFactory after validating Transactive Device.

    Once the TaValidator has done the initial on-site inspection of the Transactive
    Device including its location and the type and quality  of its power and energy
    metering, the TaValidator lets the GNodeFactory know by sending this message.
    Note the message also  includes the lat/lon of the Transactive Device. On
    receiving and validating this message, the GNodeFactory will co-sign the
    transfer and send the TaDeed to the TaDaemon address. In addition, the
    GNodeFactory creates and sends a TaTradingRights certificate to the
    TaDaemon address. Only once the GNodeFactory has verified that the
    TaDaemon address owns the TaDeed and TaTradingRights will it change
    the GNodeStatus of the associated TerminalAsset from  Pending to Active.
    [GNodeStatus](https://gridworks.readthedocs.io/en/latest/g-node-status.html)
    [TaDeed](https://gridworks.readthedocs.io/en/latest/ta-deed.html)
    [TaTradingRights](https://gridworks.readthedocs.io/en/latest/ta-trading-rights.html)
    [TaValidator](https://gridworks.readthedocs.io/en/latest/ta-validator.html)
    [TerminalAsset](https://gridworks.readthedocs.io/en/latest/terminal-asset.html)
    [Transactive Device](https://gridworks.readthedocs.io/en/latest/transactive-device.html)


    """

    MicroLat: int = Field(
        title="MicroLat",
        description="The Latitude of the Transactive Device, times 10^6",
    )
    MicroLon: int = Field(
        title="MicroLon",
        description="The Longitude of the Transactive Device, times 10^6",
    )
    ValidatorAddr: str = Field(
        title="ValidatorAddr",
        description="The Algoand address for the TaValidator who validated the location, metering and type of the Transactive Device. [More info](https://gridworks.readthedocs.io/en/latest/ta-validator.html).",
    )
    TaDaemonAddr: str = Field(
        title="TaDaemonAddr",
        description="The Algorand address for the TaDaemon which will own the TaDeed and initially the TaTradingRights), as well as holding funds on behalf of the TaOwner. [More info](https://gridworks.readthedocs.io/en/latest/ta-daemon.html).",
    )
    TaOwnerAddr: str = Field(
        title="TaOwnerAddr",
        description="The Algorand address of the entity owning the Transactive Device, and thus also the TerminalAsset",
    )
    FirstDeedTransferMtx: str = Field(
        title="FirstDeedTransferMtx",
        description="The half-signed multi transaction for transferring the TaDeed to the TaDaemon.",
    )
    TypeName: Literal["initial.tadeed.algo.transfer"] = "initial.tadeed.algo.transfer"
    Version: str = "000"

    @validator("ValidatorAddr")
    def _check_validator_addr(cls, v: str) -> str:
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"ValidatorAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("TaDaemonAddr")
    def _check_ta_daemon_addr(cls, v: str) -> str:
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"TaDaemonAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("TaOwnerAddr")
    def _check_ta_owner_addr(cls, v: str) -> str:
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"TaOwnerAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("FirstDeedTransferMtx")
    def _check_first_deed_transfer_mtx(cls, v: str) -> str:
        try:
            check_is_algo_msg_pack_encoded(v)
        except ValueError as e:
            raise ValueError(
                f"FirstDeedTransferMtx failed AlgoMsgPackEncoded format validation: {e}"
            )
        return v

    @root_validator(pre=True)
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: Is correct Multisig.
        Decoded FirstDeedTransferMtx must have type MultisigTransaction from the
        2-sig MultiAccount  [GnfAdminAddr, ValidatorAddr].
        [More info](https://gridworks.readthedocs.io/en/latest/g-node-factory.html#gnfadminaddr)
        """
        raise NotImplementedError("Implement check for axiom 1")

    @root_validator
    def check_axiom_2(cls, v: dict) -> dict:
        """
        Axiom 2: TaDaemon funded by TaOwner.
        The TaDaemonAddr was created with funding from the TaOwnerAddr, and has sufficient funding according to the GNodeFactory.
        """
        raise NotImplementedError("Implement check for axiom 2")

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class InitialTadeedAlgoTransfer_Maker:
    type_name = "initial.tadeed.algo.transfer"
    version = "000"

    def __init__(
        self,
        micro_lat: int,
        micro_lon: int,
        validator_addr: str,
        ta_daemon_addr: str,
        ta_owner_addr: str,
        first_deed_transfer_mtx: str,
    ):
        self.tuple = InitialTadeedAlgoTransfer(
            MicroLat=micro_lat,
            MicroLon=micro_lon,
            ValidatorAddr=validator_addr,
            TaDaemonAddr=ta_daemon_addr,
            TaOwnerAddr=ta_owner_addr,
            FirstDeedTransferMtx=first_deed_transfer_mtx,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: InitialTadeedAlgoTransfer) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> InitialTadeedAlgoTransfer:
        """
        Given a serialized JSON type object, returns the Python class object
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> InitialTadeedAlgoTransfer:
        d2 = dict(d)
        if "MicroLat" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MicroLat")
        if "MicroLon" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MicroLon")
        if "ValidatorAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValidatorAddr")
        if "TaDaemonAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TaDaemonAddr")
        if "TaOwnerAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TaOwnerAddr")
        if "FirstDeedTransferMtx" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FirstDeedTransferMtx")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return InitialTadeedAlgoTransfer(
            MicroLat=d2["MicroLat"],
            MicroLon=d2["MicroLon"],
            ValidatorAddr=d2["ValidatorAddr"],
            TaDaemonAddr=d2["TaDaemonAddr"],
            TaOwnerAddr=d2["TaOwnerAddr"],
            FirstDeedTransferMtx=d2["FirstDeedTransferMtx"],
            TypeName=d2["TypeName"],
            Version="000",
        )
