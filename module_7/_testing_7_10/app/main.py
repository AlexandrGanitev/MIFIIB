# from fastapi import FastAPI, APIRouter
# import app.scanner_ag_test
#
# router = APIRouter()
#
#
# @router.get("/scan")
# def do_ping(ip: str, num_of_hosts: int) :
#     for host_num in range(num_of_hosts) :
#         app.do_ping_sweep(ip, host_num)
#     print('\t\t\tStatistics:')
#     print("\nList of existing IP addresses:")
#     print(app.scanner_ag_test.existing_IP_addresses)
#     print('*' * 70 + '\n')
#     return app.scanner_ag_test.existing_IP_addresses
#
#
# @router.get("/sendhttp")
# def do_send_http(target: str, method: str, headers=None, payload=None) :
#     app.send_http_request(target, method, headers, payload)
#
#
# appl = FastAPI()
# appl.include_router(router)

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Привет": "От Александра"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
