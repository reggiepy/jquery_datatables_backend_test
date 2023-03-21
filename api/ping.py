# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2023/2/28 10:08

from fastapi import Request, Response
from fastapi.routing import APIRouter

api = APIRouter(tags=["test"])


@api.get("/ping/")
def ping(request: Request, response: Response):
    return "pong"
