"""Tests g.node.gt type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gridworks.enums import GNodeRole
from gridworks.enums import GNodeStatus
from gridworks.errors import SchemaError
from gridworks.types import GNodeGt_Maker as Maker


def test_g_node_gt_generated() -> None:
    d = {
        "GNodeId": "9405686a-14fd-4aef-945b-cd7c97903f14",
        "Alias": "d1.iso.me.orange.ta",
        "StatusGtEnumSymbol": "3661506b",
        "RoleGtEnumSymbol": "0f8872f7",
        "GNodeRegistryAddr": "MONSDN5MXG4VMIOHJNCJJBVASG7HEZQSCEIKJAPEPVI5ZJUMQGXQKSOAYU",
        "PrevAlias": "d1",
        "GpsPointId": "50f3f6e8-5937-47c2-8d05-06525ef6467d",
        "ComponentId": "19d3dd42-14de-427f-a489-d96b404ae3c5",
        "DisplayName": "Simulated Freedom House 1",
        "OwnershipDeedNftId": 5,
        "OwnerAddr": "7QQT4GN3ZPAQEFCNWF5BMF7NULVK3CWICZVT4GM3BQRISD52YEDLWJ4MII",
        "OwnershipDeedValidatorAddr": "RNMHG32VTIHTC7W3LZOEPTDGREL5IQGK46HKD3KBLZHYQUCAKLMT4G5ALI",
        "DaemonAddr": "7QQT4GN3ZPAQEFCNWF5BMF7NULVK3CWICZVT4GM3BQRISD52YEDLWJ4MII",
        "TradingRightsNftId": 1,
        "TypeName": "g.node.gt",
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
        g_node_id=gtuple.GNodeId,
        alias=gtuple.Alias,
        status=gtuple.Status,
        role=gtuple.Role,
        g_node_registry_addr=gtuple.GNodeRegistryAddr,
        prev_alias=gtuple.PrevAlias,
        gps_point_id=gtuple.GpsPointId,
        component_id=gtuple.ComponentId,
        display_name=gtuple.DisplayName,
        ownership_deed_nft_id=gtuple.OwnershipDeedNftId,
        owner_addr=gtuple.OwnerAddr,
        ownership_deed_validator_addr=gtuple.OwnershipDeedValidatorAddr,
        daemon_addr=gtuple.DaemonAddr,
        trading_rights_nft_id=gtuple.TradingRightsNftId,
    ).tuple
    assert t == gtuple

    ######################################
    # Dataclass related tests
    ######################################

    dc = Maker.tuple_to_dc(gtuple)
    assert gtuple == Maker.dc_to_tuple(dc)
    assert Maker.type_to_dc(Maker.dc_to_type(dc)) == dc

    ######################################
    # SchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["GNodeId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Alias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StatusGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RoleGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["GNodeRegistryAddr"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "PrevAlias" in d2.keys():
        del d2["PrevAlias"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "GpsPointId" in d2.keys():
        del d2["GpsPointId"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "ComponentId" in d2.keys():
        del d2["ComponentId"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "DisplayName" in d2.keys():
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "OwnershipDeedNftId" in d2.keys():
        del d2["OwnershipDeedNftId"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "OwnerAddr" in d2.keys():
        del d2["OwnerAddr"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "OwnershipDeedValidatorAddr" in d2.keys():
        del d2["OwnershipDeedValidatorAddr"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "DaemonAddr" in d2.keys():
        del d2["DaemonAddr"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "TradingRightsNftId" in d2.keys():
        del d2["TradingRightsNftId"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, StatusGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).Status = GNodeStatus.default()

    d2 = dict(d, RoleGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).Role = GNodeRole.default()

    d2 = dict(d, OwnershipDeedNftId="5.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TradingRightsNftId="1.1")
    with pytest.raises(ValidationError):
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

    d2 = dict(d, GNodeId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Alias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, PrevAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, GpsPointId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ComponentId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
