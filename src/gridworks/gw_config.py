"""Settings for the GNodeFactory, readable from environment and/or from env files."""

import datetime
from algosdk import account
from pydantic import BaseModel
from pydantic import BaseSettings
from pydantic import SecretStr
from pydantic import root_validator

from gridworks.enums import GNodeRole
from gridworks.enums import UniverseType


DEFAULT_ENV_FILE = ".env"


def check_is_algo_secret_key_format(v: str) -> None:
    try:
        b = account.address_from_private_key(v)
    except Exception as e:
        raise ValueError(
            f"Not Algorand Secret Key format! Generate one by: \n"
            f"from gridworks.algo_utils import BasicAccount\n\n"
            f"BasicAccount().sk\n"
            f"incorrect sk: {v}"
        )


def check_is_left_right_dot(v: str) -> None:
    """
    LeftRightDot format: Lowercase alphanumeric words separated by periods,
    most significant word (on the left) starting with an alphabet character.

    Raises:
        ValueError: if not LeftRightDot format
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate {v} into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(f"Most significant word of {v} must start with alphabet char.")
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of {v} split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of {v} must be lowercase.")


def check_is_reasonable_unix_time_s(v: int) -> None:
    """
    ReasonableUnixTimeS format: time in unix seconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeS format
    """
    from datetime import datetime, timezone
    start_date = datetime(2000, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(3000, 1, 1, tzinfo=timezone.utc)

    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    if v < start_timestamp:
        raise ValueError(f"{v} must be after Jan 1 2000")
    if v > end_timestamp:
        raise ValueError(f"{v} must be before Jan 1 3000")

def check_g_node_alias(alias: str, universe_type: UniverseType) -> None:
    check_is_left_right_dot(alias)
    first_word = alias.split(".")[0]
    if universe_type == UniverseType.Dev:
        if not first_word.startswith("d"):
            raise ValueError(
                f"Bad alias {alias} ... Dev universe GNode alias must start with d."
            )
    elif universe_type == UniverseType.Hybrid:
        if not first_word.startswith("h"):
            raise ValueError(
                f"Bad alias {alias} ... Hybrid universe GNode alias must start with h."
            )
    elif universe_type == UniverseType.Production:
        if not first_word == "w":
            raise ValueError(
                f"Bad alias {alias} ... Production universe GNode alias must have w as first word."
            )


class Public(BaseModel):
    """
    Publicly available information about the GNodeFactory, including:
      - GnfAdminAddr
      - GnfApiRoot
      - TaValidatorFundingThresholdAlgos
      - TaDeedConsiderationAlgos

    Also includes useful information shartcuts for running the simulated Millinocket
    demo. In this demo there is only one MarketMaker, and one TaValidator.
    Public Algorand addresses and ApiRoots are included for both.
    """

    gnf_api_root: str = "http://localhost:8000"
    dev_market_maker_api_root: str = "http://localhost:7997"
    dev_ta_validator_api_root: str = "http://localhost:8001"
    gnf_admin_addr: str = "RNMHG32VTIHTC7W3LZOEPTDGREL5IQGK46HKD3KBLZHYQUCAKLMT4G5ALI"
    gnr_addr: str = "X2ASUAUPK5ICMGDXQZQKBPSXWEJLBA4KKQ2TXW2KWO2JQTLY3J2Q4S33WE"
    dev_market_maker_addr: str = (
        "JMEUH2AXM6UGRJO2DBZXDOA2OMIWQFNQZ54LCVC4GQX6QDOX5Z6JRGMWFA"
    )
    dev_ta_validator_addr: str = (
        "7QQT4GN3ZPAQEFCNWF5BMF7NULVK3CWICZVT4GM3BQRISD52YEDLWJ4MII"
    )
    dev_ta_validator_multi_addr: str = (
        "Y5TRQXIJHWJ4OHCZSWP4PZTCES5VWOF2KDTNYSMU5HLAUXBFQQDX6IR5KM'"
    )
    ta_validator_funding_threshold_algos: int = 100
    ta_deed_consideration_algos: int = 50
    universe: str = "dev"
    gnf_graveyard_addr: str = (
        "COA6SYUOBE33F5JDYEGC5XAD43QRG3VGHNNQXLYWFSSQEHDQ5HJ52NDNPI"
    )
    algod_address: str = "http://localhost:4001"
    kmd_address: str = "http://localhost:4002"
    gen_kmd_wallet_name: str = "unencrypted-default-wallet"


class AlgoApiSecrets(BaseModel):
    algod_token: SecretStr = SecretStr(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    )
    kmd_token: SecretStr = SecretStr(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    )
    gen_kmd_wallet_password: SecretStr = SecretStr("")


class VanillaSettings(BaseSettings):
    algo_api_secrets: AlgoApiSecrets = AlgoApiSecrets()
    public: Public = Public()

    class Config:
        env_prefix = "VANILLA_"
        env_nested_delimiter = "__"


class RabbitBrokerClient(BaseModel):
    """Settings for connecting to a Rabbit Broker"""

    url: SecretStr = SecretStr("amqp://smqPublic:smqPublic@localhost:5672/d1__1")


class GNodeSettings(BaseSettings):
    """
    Template settings for a GNode.
    """

    public: Public = Public()
    algo_api_secrets: AlgoApiSecrets = AlgoApiSecrets()
    rabbit: RabbitBrokerClient = RabbitBrokerClient()
    redis_endpoint: str = "localhost"

    g_node_alias: str = "d1.isone.unknown.gnode"
    g_node_id: str = "e23eb2ec-4064-4921-89d4-b006edc81216"
    g_node_instance_id: str = "00000000-0000-0000-0000-000000000000"
    g_node_role_value: str = "GNode"
    sk: SecretStr = SecretStr(
        "3g+IYDCVM84Ady7a8fGImRkEZ77+a4e3i14ub0QMjM/JKlzB2GNdv0S+lqMsYgPiGbd7aAp5943X5NzvdQJohw=="
    )
    # Secret key for public Algorand adress ZEVFZQOYMNO36RF6S2RSYYQD4IM3O63IBJ47PDOX4TOO65ICNCDUF4HMLE
    universe_type_value: str = "Dev"
    my_super_alias: str = "d1.super1"
    my_time_coordinator_alias: str = "d1.time"
    initial_time_unix_s = int(datetime.datetime(2020, 1, 1, 4, 20, tzinfo=datetime.timezone.utc).timestamp())

    log_level: str = "INFO"
    minute_cron_file: str = "cron_last_minute.txt"
    hour_cron_file: str = "cron_last_hour.txt"
    day_cron_file: str = "cron_last_day.txt"

    @root_validator
    def validate_setting_axioms(cls, values):
        """
        Validates the following:
            - universe_type_value belongs to the GridWorks UniverseType enum
            - g_node_role_value belongs to the GridWOrks GNodeRole enum
            - All GNodeAliases (self, my time coordinator, my super) have the correct
            LeftRightDot format and match the alias pattern for the universe type
            - sk.get_secret_value() has the format of an Algorand secret key
            - initial_time_unix_s is a reasonable unix time in ms
        """
        g_node_alias = values.get("g_node_alias")
        g_node_role_value = values.get("g_node_role_value")
        my_super_alias = values.get("my_super_alias")
        my_time_coordinator_alias = values.get("my_time_coordinator_alias")
        sk = values.get("sk")
        initial_time_unix_s = values.get("initial_time_unix_s")
        universe_type_value = values.get("universe_type_value")
        if universe_type_value not in UniverseType.values():
            raise ValueError("universe_type_value must belong to UniverseType.values()")
        universe_type = UniverseType(universe_type_value)
        if g_node_role_value not in GNodeRole.values():
            raise ValueError("g_node_role_value must belong to GNodeRole.values()")
        check_g_node_alias(alias=g_node_alias, universe_type=universe_type)
        check_g_node_alias(alias=my_time_coordinator_alias, universe_type=universe_type)
        check_g_node_alias(alias=my_super_alias, universe_type=universe_type)
        check_is_algo_secret_key_format(sk.get_secret_value())
        check_is_reasonable_unix_time_s(initial_time_unix_s)
        return values

    class Config:
        env_prefix = "GNODE_"
        env_nested_delimiter = "__"


class SupervisorSettings(BaseSettings):
    g_node_alias: str = "d1.isone.ver.keene.super1"
    g_node_id: str = "664a3250-ce51-4fe3-9ce9-a4b6416451fb"
    g_node_instance_id: str = "20e7edec-05e5-4152-bfec-ec21ddd2e3dd"
    supervisor_container_id: str = "995b0334-9940-424f-8fb1-4745e52ba295"
    g_node_role_value: str = "Supervisor"
    my_time_coordinator_alias = "d1.time"
    log_level: str = "INFO"
    universe_type_value: str = "Dev"
    world_instance_name: str = "d1__1"
    rabbit: RabbitBrokerClient = RabbitBrokerClient()

    class Config:
        env_prefix = "SUPER_"
        env_nested_delimiter = "__"
