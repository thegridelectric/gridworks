from gw.named_types import GwBase


def test_gw_base() -> None:
    bytes = '{"TypeName":"gw.base","Version":"000"}'.encode()
    assert GwBase.from_type(bytes).to_type() == bytes
