from typing import Any
from demon.pinapi import PinMachine
from fastapi import APIRouter

router = APIRouter()


@router.get("/on_light")
def on_light(num: int = 0) -> Any:
    pin = PinMachine(num)
    print(f'on_light  {pin}')
    return {'result': True}


@router.get("/off_light")
def off_light(num: int = 0) -> Any:
    pin = PinMachine(num)
    print(f'off_light {pin}')
    return {'result': True}


@router.get("/water_on_pin")
def water_on_pin(num: int = 0) -> Any:
    pin = PinMachine(num)
    print(f'water_on_pin {pin}')
    return {'result': True}


@router.get("/water_off_pin")
def water_off_pin(num: int = 0) -> Any:
    pin = PinMachine(num)
    print(f'water_off_pin  {pin}')
    return {'result': True}


@router.get("/water_time_pin")
def water_time_pin(
        num: int = 0,
        tim: int = 0,
) -> Any:
    pin = PinMachine(num)
    print(f'water_time_pin  {pin} {tim}')
    return {'result': True}


@router.get("/info")
def info() -> Any:
    print('info')
    return {'result': True}
