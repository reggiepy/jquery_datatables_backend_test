# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2023/2/17 14:57


from fastapi.routing import APIRouter

from api import ping
from api import datatables

api_router = APIRouter(prefix="/v1")
api_router.include_router(ping.api)
api_router.include_router(datatables.api, prefix="/datatables")
