from functools import lru_cache

from fastapi import FastAPI
from fastapi import HTTPException

import gridworks.gw_config as config
from gridworks.types import HeartbeatA
from gridworks.types import HeartbeatA_Maker
from gridworks.types import Ready
from gridworks.types import Ready_Maker
from gridworks.utils import RestfulResponse


# Create FasatAPI instance
app = FastAPI()

payload = HeartbeatA(MyHex="a", YourLastHex="b")


@lru_cache()
def get_settings():
    return config.GNodeSettings()


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
