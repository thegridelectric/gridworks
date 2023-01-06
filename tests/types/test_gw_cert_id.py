"""Tests gw.cert.id type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gridworks.enums import AlgoCertType
from gridworks.errors import SchemaError
from gridworks.types import GwCertId_Maker as Maker


def test_gw_cert_id_generated() -> None:
    d = {
        "TypeGtEnumSymbol": "086b5165",
        "Idx": 10,
        "Addr": "7QQT4GN3ZPAQEFCNWF5BMF7NULVK3CWICZVT4GM3BQRISD52YEDLWJ4MII",
        "TypeName": "gw.cert.id",
        "Version": "000",
    }

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # test Maker init
    t = Maker(
        type=gtuple.Type,
        idx=gtuple.Idx,
        addr=gtuple.Addr,
    ).tuple
    assert t == gtuple

    ######################################
    # SchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TypeGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "Idx" in d2.keys():
        del d2["Idx"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "Addr" in d2.keys():
        del d2["Addr"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TypeGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).Type = AlgoCertType.default()

    d2 = dict(d, Idx="10.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
