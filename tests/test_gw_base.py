from gw.named_types import GwBase


def test_gw_base() -> None:
    bytes = b'{"TypeName":"gw.base","Version":"000"}'
    assert GwBase.from_type(bytes).to_type() == bytes
