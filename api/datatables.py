# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2023/2/17 14:10
from fastapi import Request, Query
from fastapi.routing import APIRouter

api = APIRouter(tags=["rpc"])


@api.get(
    '/test/',
    description="zero rpc call",
    dependencies=[]
)
async def common_rpc(
        request: Request,
        draw: int = Query(...),
        start: int = Query(...),
        length: int = Query(...),
):
    print(start, length)
    print(dict(request.query_params))
    data = [
        [
            "Garrett",
            "Winters",
            "Accountant",
            "Tokyo",
            "25th Jul 11",
            "$170,750"
        ],
        [
            "Airi",
            "Satou",
            "Accountant",
            "Tokyo",
            "28th Nov 08",
            "$162,700"
        ],
        [
            "Angelica",
            "Ramos",
            "Chief Executive Officer (CEO)",
            "London",
            "9th Oct 09",
            "$1,200,000"
        ],
        [
            "Paul",
            "Byrd",
            "Chief Financial Officer (CFO)",
            "New York",
            "9th Jun 10",
            "$725,000"
        ],
        [
            "Yuri",
            "Berry",
            "Chief Marketing Officer (CMO)",
            "New York",
            "25th Jun 09",
            "$675,000"
        ],
        [
            "Fiona",
            "Green",
            "Chief Operating Officer (COO)",
            "San Francisco",
            "11th Mar 10",
            "$850,000"
        ],
        [
            "Donna",
            "Snider",
            "Customer Support",
            "New York",
            "25th Jan 11",
            "$112,000"
        ],
        [
            "Serge",
            "Baldwin",
            "Data Coordinator",
            "Singapore",
            "9th Apr 12",
            "$138,575"
        ],
        [
            "Gavin",
            "Joyce",
            "Developer",
            "Edinburgh",
            "22nd Dec 10",
            "$92,575"
        ],
        [
            "Suki",
            "Burks",
            "Developer",
            "London",
            "22nd Oct 09",
            "$114,500"
        ]
    ]
    start = start * length
    end = start + length
    print(start, end, data[start: end])
    return {
        "draw": draw,  # Datatables发送的draw是多少那么服务器就返回多少
        # 作者出于安全的考虑，强烈要求把这个转换为整形，即数字后再返回，而不是纯粹的接受然后返回，这是 为了防止跨站脚本（XSS）攻击。
        "recordsTotal": len(data),  # 总数
        "recordsFiltered": len(data),  # 过滤后记录数量
        "data": data[start: end]
    }
