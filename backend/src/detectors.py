from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel

from nicos.clients.http.backend.src.client import client

router = APIRouter(prefix="/detectors",)


@router.get("/")
async def list_detectors():
    detectors = client.getDeviceParam('exp', 'detlist')
    return detectors


@router.get("/{detector}")
async def readarray():
    value = client.eval()
    return value


@router.delete("/{detector}")
async def remove_detector():
    #TODO
    return 200


class CountCommand(BaseModel):
    preset: str
    value: Union[int, float]


@router.patch("/{detector}")
async def count(detector:str, count: CountCommand):
    print(f'count({detector},{count.preset}={count.value}')
    client.ask('queue', '', f'count({detector},{count.preset}={count.value})')
    # check for success/failure
    return 200
