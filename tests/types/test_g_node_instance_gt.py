"""Tests g.node.instance.gt type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gridworks.enums import GniStatus
from gridworks.enums import StrategyName
from gridworks.errors import SchemaError
from gridworks.types import GNodeInstanceGt_Maker as Maker


def test_g_node_instance_gt_generated() -> None:
    d = {
        "GNodeInstanceId": "76d2a9b9-7804-4bdb-b712-8710a1e37252",
        "GNode": {
            "GNodeId": "7b1df82e-10c5-49d9-8d02-1e837e31b87e",
            "Alias": "d1",
            "GNodeRegistryAddr": "MONSDN5MXG4VMIOHJNCJJBVASG7HEZQSCEIKJAPEPVI5ZJUMQGXQKSOAYU",
            "TypeName": "g.node.gt",
            "Version": "000",
            "StatusGtEnumSymbol": "a2cfc2f7",
            "RoleGtEnumSymbol": "3901c7d2",
        },
        "StrategyGtEnumSymbol": "00000000",
        "StatusGtEnumSymbol": "00000000",
        "SupervisorContainerId": "299ed6df-183d-4230-b60d-fd2eae34b1cd",
        "StartTimeUnixS": 1670025409,
        "EndTimeUnixS": 0,
        "AlgoAddress": "4JHRDNY4F6RCVGPALZULZWZNVP3OKT3DATEOLINCGILVPGHUOFY7KCHVIQ",
        "TypeName": "g.node.instance.gt",
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
        g_node_instance_id=gtuple.GNodeInstanceId,
        g_node=gtuple.GNode,
        strategy=gtuple.Strategy,
        status=gtuple.Status,
        supervisor_container_id=gtuple.SupervisorContainerId,
        start_time_unix_s=gtuple.StartTimeUnixS,
        end_time_unix_s=gtuple.EndTimeUnixS,
        algo_address=gtuple.AlgoAddress,
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
    del d2["GNodeInstanceId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["GNode"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StrategyGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StatusGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SupervisorContainerId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StartTimeUnixS"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["EndTimeUnixS"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "AlgoAddress" in d2.keys():
        del d2["AlgoAddress"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, StrategyGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).Strategy = StrategyName.default()

    d2 = dict(d, StatusGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).Status = GniStatus.default()

    d2 = dict(d, StartTimeUnixS="1670025409.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EndTimeUnixS="0.1")
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

    d2 = dict(d, GNodeInstanceId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SupervisorContainerId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StartTimeUnixS=32503683600)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
