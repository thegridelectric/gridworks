"""Settings for the GNodeFactory, readable from environment and/or from env files."""

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
