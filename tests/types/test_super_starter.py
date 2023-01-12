"""Tests super.starter type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gridworks.errors import SchemaError
from gridworks.types import SuperStarter_Maker as Maker


def test_super_starter_generated() -> None:
    d = {
        "SupervisorContainer": {
            "SupervisorContainerId": "995b0334-9940-424f-8fb1-4745e52ba295",
            "WorldInstanceName": "d1__1",
            "SupervisorGNodeInstanceId": "20e7edec-05e5-4152-bfec-ec21ddd2e3dd",
            "SupervisorGNodeAlias": "d1.isone.ver.keene.super1",
            "TypeName": "supervisor.container.gt",
            "Version": "000",
            "StatusGtEnumSymbol": "f48cff43",
        },
        "GniList": [],
        "AliasWithKeyList": [],
        "KeyList": [],
        "TypeName": "super.starter",
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
        supervisor_container=gtuple.SupervisorContainer,
        gni_list=gtuple.GniList,
        alias_with_key_list=gtuple.AliasWithKeyList,
        key_list=gtuple.KeyList,
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
    del d2["SupervisorContainer"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["GniList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AliasWithKeyList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["KeyList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, GniList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, GniList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, GniList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, AliasWithKeyList=["a.b-h"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
