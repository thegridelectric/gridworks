"""Settings for the GNodeFactory, readable from environment and/or from env files."""
import pendulum
from pydantic import BaseModel
from pydantic import BaseSettings
from pydantic import SecretStr


DEFAULT_ENV_FILE = ".env"


class Public(BaseModel):
    """This class is the publicly available information about the GNodeFactory"""

    algod_address: str = "http://localhost:4001"
    kmd_address: str = "http://localhost:4002"
    gen_kmd_wallet_name: str = "unencrypted-default-wallet"
    universe: str = "dev"
    gnf_g_node_alias: str = "dwgps.gnf"
    gnf_admin_addr: str = "RNMHG32VTIHTC7W3LZOEPTDGREL5IQGK46HKD3KBLZHYQUCAKLMT4G5ALI"
    gnf_graveyard_addr: str = (
        "COA6SYUOBE33F5JDYEGC5XAD43QRG3VGHNNQXLYWFSSQEHDQ5HJ52NDNPI"
    )
    gnr_addr: str = "X2ASUAUPK5ICMGDXQZQKBPSXWEJLBA4KKQ2TXW2KWO2JQTLY3J2Q4S33WE"
    gnf_validator_funding_threshold_algos: int = 100
    ta_deed_consideration_algos: int = 50
    gnf_api_root: str = "http://localhost:8000"


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
    g_node_alias: str = "d1.isone.unknown.gnode"
    g_node_id: str = "e23eb2ec-4064-4921-89d4-b006edc81216"
    g_node_instance_id: str = "97eba574-bd20-45b5-bf82-9ba2f492d8f6"
    g_node_role_value: str = "GNode"
    sk: SecretStr = SecretStr(
        "K6iB3AHmzSQ8wDE91QdUfaheDMEtf2WJUMYeeRptKxHiTxG3HC+iKpngXmi82y2r9uVPYwTI5aGiMhdXmPRxcQ=="
    )
    my_super_alias: str = "d1.super1"
    time_coordinator_alias = "d1.time"
    initial_time_unix_s = pendulum.datetime(
        year=2020, month=1, day=1, hour=4, minute=20
    ).int_timestamp
    log_level: str = "INFO"
    universe_type_value: str = "Dev"
    rabbit: RabbitBrokerClient = RabbitBrokerClient()
    public: Public = Public()
    algo_api_secrets: AlgoApiSecrets = AlgoApiSecrets()

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
    world_instance_alias: str = "d1__1"
    rabbit: RabbitBrokerClient = RabbitBrokerClient()

    class Config:
        env_prefix = "SUPER_"
        env_nested_delimiter = "__"
