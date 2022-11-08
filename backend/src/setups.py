from fastapi import APIRouter
from nicos.clients.http.backend.src.client import client, log

router = APIRouter(prefix="/setups",)


@router.get("/")
async def list_setups():
    # log.debug(client.getDeviceParams(dev) for dev in client.getDeviceList())
    return {'setups': client.ask('eval', 'session.getSetupInfo()', 404)}


@router.get("/{setup}")
async def get_setup(setup: str):

    setups = client.ask('eval', 'session.getSetupInfo()', {})
    if setup not in setups:
        log.error(f'{setup} not loaded')
        return 404
    value = setups[setup]
    return {setup: value}


@router.delete("/{setup}")
async def remove_setup(setup: str):
    client.ask('queue', '', f'RemoveSetup("{setup}")')
    return 200


@router.post("/{setup}")
async def create_setup(setup: str):
    client.ask('queue', '', f'AddSetup("{setup}")')
    return 200


@router.get("/{setup}/devices")
async def get_setup(setup: str):

    setups = client.ask('eval', 'session.getSetupInfo()', {})
    if setup not in setups:
        log.error(f'{setup} not loaded')
        return 404
    value = setups[setup].get('devices')
    return {setup: value}
