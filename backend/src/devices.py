import json
from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel

from nicos.clients.http.backend.src.client import client

router = APIRouter(prefix="/devices",)


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, frozenset):
            return list(obj)
        try:
            encoded = json.JSONEncoder.default(self, obj)
        except TypeError as _:
            encoded = None
        return encoded


@router.get("/")
async def list_devices():
    devices = client.ask('eval', 'session.explicit_devices', {})
    items = []
    for devname in sorted([d.lower() for d in devices]):
        items.append(client.getDeviceParams(devname))
        # items.update({devname: client.getDeviceParams(devname)})
    return json.loads(json.dumps(items, cls=SetEncoder))
    # return items

@router.get("/{device}")
async def device(device:str):
    return client.getDeviceParams(device)


@router.get("/{device}/{param}")
async def device_param(device:str, param: str):
    return client.getDeviceParams(device).get(param)


actions_factory = dict()


def register(key):
    def inner_decorator(processor):
        global actions_factory
        actions_factory.update({key: processor})
        return processor
    return inner_decorator


class Action(BaseModel):
    param: str
    value: Union[int, float, str, list, None] = None


@register('target')
def drive_device(device:str, action: Action):
    return f'maw({device}, {action.value})'


def default_action(device:str, action: Action):
    return f'{device}.{action.param}={action.value}'


@router.patch("/{device}")
async def do_something(device: str, action: Action):
    req = actions_factory.get(action.param, default_action)(device, action)
    client.ask('queue', '', req)
    # check for success/failure
    return 200