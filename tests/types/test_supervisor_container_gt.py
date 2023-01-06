"""Tests supervisor.container.gt type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gridworks.enums import SupervisorContainerStatus
from gridworks.errors import SchemaError
from gridworks.types import SupervisorContainerGt_Maker as Maker


def test_supervisor_container_gt_generated() -> None:
    d = {
        "SupervisorContainerId": "da2dafe0-b5c8-4c36-984c-ae653a29bfcc",
        "StatusGtEnumSymbol": "00000000",
        "WorldInstanceName": "d1__1",
        "SupervisorGNodeInstanceId": "aac80de4-91cf-48e7-9bef-d469eba989ad",
        "SupervisorGNodeAlias": "d1.super1",
        "TypeName": "supervisor.container.gt",
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
        supervisor_container_id=gtuple.SupervisorContainerId,
        status=gtuple.Status,
        world_instance_name=gtuple.WorldInstanceName,
        supervisor_g_node_instance_id=gtuple.SupervisorGNodeInstanceId,
        supervisor_g_node_alias=gtuple.SupervisorGNodeAlias,
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
    del d2["SupervisorContainerId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["StatusGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["WorldInstanceName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SupervisorGNodeInstanceId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SupervisorGNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, StatusGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).Status = SupervisorContainerStatus.default()

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, SupervisorContainerId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SupervisorGNodeInstanceId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SupervisorGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
