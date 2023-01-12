from functools import lru_cache

from fastapi import FastAPI
from fastapi import HTTPException

import gridworks.gw_config as config
from gridworks.types import GNodeGt
from gridworks.types import GNodeGt_Maker
from gridworks.types import GNodeInstanceGt
from gridworks.types import GNodeInstanceGt_Maker
from gridworks.types import GwCertId
from gridworks.types import GwCertId_Maker
from gridworks.types import HeartbeatA
from gridworks.types import HeartbeatA_Maker
from gridworks.types import Ready
from gridworks.types import Ready_Maker
from gridworks.types import SimTimestep
from gridworks.types import SimTimestep_Maker
from gridworks.types import SuperStarter
from gridworks.types import SuperStarter_Maker
from gridworks.types import SupervisorContainerGt
from gridworks.types import SupervisorContainerGt_Maker
from gridworks.types import TavalidatorcertAlgoCreate
from gridworks.types import TavalidatorcertAlgoCreate_Maker
from gridworks.types import TavalidatorcertAlgoTransfer
from gridworks.types import TavalidatorcertAlgoTransfer_Maker
from gridworks.utils import RestfulResponse


# Create FasatAPI instance
app = FastAPI()

payload = HeartbeatA(MyHex="a", YourLastHex="b")


@lru_cache()
def get_settings():
    return config.GNodeSettings()


@app.post("/g-node-gt/", response_model=RestfulResponse)
async def g_node_gt_received(
    d: dict,
):
    try:
        payload = GNodeGt_Maker.dict_to_tuple(d)
    except ValueError as e:
        raise HttpException(status_code=422, detail=f"{e}")
    if payload.Version not in ["000"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['000'], not '{payload.Version}'!",
        )

    if payload.Version == "000":
        note = "Valid payload"

    else:
        note = f"Version {payload.Version} is out of date. Payload updated to 000"

        payload = GNodeGt_Maker.type_to_tuple(payload.as_type())

    return RestfulResponse(
        Note=note,
        PayloadTypeName=GNodeGt_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/g-node-instance-gt/", response_model=RestfulResponse)
async def g_node_instance_gt_received(
    d: dict,
):
    try:
        payload = GNodeInstanceGt_Maker.dict_to_tuple(d)
    except ValueError as e:
        raise HttpException(status_code=422, detail=f"{e}")
    if payload.Version not in ["000"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['000'], not '{payload.Version}'!",
        )

    if payload.Version == "000":
        note = "Valid payload"

    else:
        note = f"Version {payload.Version} is out of date. Payload updated to 000"

        payload = GNodeInstanceGt_Maker.type_to_tuple(payload.as_type())

    return RestfulResponse(
        Note=note,
        PayloadTypeName=GNodeInstanceGt_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/gw-cert/", response_model=RestfulResponse)
async def gw_cert_received(
    d: dict,
):
    try:
        payload = GwCertId_Maker.dict_to_tuple(d)
    except ValueError as e:
        raise HttpException(status_code=422, detail=f"{e}")
    if payload.Version not in ["000"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['000'], not '{payload.Version}'!",
        )

    if payload.Version == "000":
        note = "Valid payload"

    else:
        note = f"Version {payload.Version} is out of date. Payload updated to 000"
        payload = GwCertId_Maker.type_to_tuple(payload.as_type())

    return RestfulResponse(
        Note=note,
        PayloadTypeName=GNodeInstanceGt_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/heartbeat-a/", response_model=RestfulResponse)
async def heartbeat_a_received(
    payload: HeartbeatA,
):
    if payload.Version not in ["001", "100"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['001', '100'], not '{payload.Version}'!",
        )

    if payload.Version == "100":
        note = "Valid payload"

    else:
        note = f"Version {payload.Version} is out of date. Payload updated to 100"
        payload = HeartbeatA_Maker.type_to_tuple(payload.as_type())

    return RestfulResponse(
        Note=note,
        PayloadTypeName=HeartbeatA_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/ready/", response_model=RestfulResponse)
async def ready_received(
    payload: Ready,
):
    if payload.Version not in ["001"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['001'], not {payload.Version}!",
        )

    return RestfulResponse(
        Note="Valid Payload",
        PayloadTypeName=Ready_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/sim-timestep/", response_model=RestfulResponse)
async def sim_timestep_received(
    payload: SimTimestep,
):
    if payload.Version not in ["000"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['000'], not '{payload.Version}'!",
        )

    if payload.Version == "000":
        note = "Valid payload"

    else:
        note = f"Version {payload.Version} is out of date. Payload updated to 000"
        payload = SimTimestep_Maker.type_to_tuple(payload.as_type())

    return RestfulResponse(
        Note=note,
        PayloadTypeName=SimTimestep_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/super-starter/", response_model=RestfulResponse)
async def super_starter_received(
    d: dict,
):
    try:
        payload = SuperStarter_Maker.dict_to_tuple(d)
    except ValueError as e:
        raise HttpException(status_code=422, detail=f"{e}")
    if payload.Version not in ["000"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['000'], not '{payload.Version}'!",
        )

    if payload.Version == "000":
        note = "Valid payload"

    else:
        note = f"Version {payload.Version} is out of date. Payload updated to 000"
        payload = SuperStarter_Maker.type_to_tuple(payload.as_type())

    return RestfulResponse(
        Note=note,
        PayloadTypeName=SuperStarter_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/supervisor-container-gt/", response_model=RestfulResponse)
async def supervisor_container_gt_received(
    d: dict,
):
    try:
        payload = SupervisorContainerGt_Maker.dict_to_tuple(d)
    except ValueError as e:
        raise HttpException(status_code=422, detail=f"{e}")
    if payload.Version not in ["000"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['000'], not '{payload.Version}'!",
        )

    if payload.Version == "000":
        note = "Valid payload"

    else:
        note = f"Version {payload.Version} is out of date. Payload updated to 000"
        payload = SupervisorContainerGt_Maker.type_to_tuple(payload.as_type())

    return RestfulResponse(
        Note=note,
        PayloadTypeName=SupervisorContainerGt_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/tavalidatorcert-algo-create/", response_model=RestfulResponse)
async def tavalidatorcert_algo_create_received(
    payload: TavalidatorcertAlgoCreate,
):
    if payload.Version not in ["000"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['000'], not '{payload.Version}'!",
        )

    if payload.Version == "000":
        note = "Valid payload"

    else:
        note = f"Version {payload.Version} is out of date. Payload updated to 000"
        payload = TavalidatorcertAlgoCreate_Maker.type_to_tuple(payload.as_type())

    return RestfulResponse(
        Note=note,
        PayloadTypeName=TavalidatorcertAlgoCreate_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/tavalidatorcert-algo-transfer/", response_model=RestfulResponse)
async def tavalidatorcert_algo_transfer_received(
    payload: TavalidatorcertAlgoTransfer,
):
    if payload.Version not in ["000"]:
        raise HTTPException(
            status_code=422,
            detail=f"Existing versions include ['000'], not '{payload.Version}'!",
        )

    if payload.Version == "000":
        note = "Valid payload"

    else:
        note = f"Version {payload.Version} is out of date. Payload updated to 000"
        payload = TavalidatorcertAlgoTransfer_Maker.type_to_tuple(payload.as_type())

    return RestfulResponse(
        Note=note,
        PayloadTypeName=TavalidatorcertAlgoTransfer_Maker.type_name,
        PayloadAsDict=payload.as_dict(),
    )


@app.post("/python-sdk-types/", response_model=RestfulResponse)
async def list_all(
    payload2: GNodeInstanceGt, payload3: GwCertId, payload4: SuperStarter
):
    """
    This is just a hack so that all the Types show up at api-endpoint/docs#/
    """

    return RestfulResponse(
        Note=" This is just a hack so that all the Types show up at api-endpoint/docs#/"
    )
