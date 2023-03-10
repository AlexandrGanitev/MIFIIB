# coding=utf-8
from http.server import HTTPServer, BaseHTTPRequestHandler
from app.scanner_ag import do_ping_sweep, sent_http_request

# Функция квадрата
def sqr(num):
   return num * num


# Функция прибавления
def number_plus(num):
   return 2 * num


# Обработка запросов
class ServiceHandler(BaseHTTPRequestHandler):
   # Устанавливаем параметры заголовков для ответа
   def set_headers(self):
       self.send_response(200)
       self.send_header("Content-type", "text/json")
       length = int(self.headers["Content-Length"])
       content = self.rfile.read(length)
       temp = str(content).strip('b\'')
       self.end_headers()
       return temp

   # Обрабатываем GET запросы
   def do_GET(self):
       temp = self.set_headers()
       number_sqr = sqr(int(temp))
       # Если получаем GET запрос, то возводим полученное число в квадрат
       self.wfile.write((f"Complete! Squared number is: {number_sqr}").encode())

   # Обрабатываем POST запросы
   def do_POST(self):
       temp = self.set_headers()
       numberx2 = number_plus(int(temp))
       # Если получаем POST запрос, то удваиваем полученное число
       self.wfile.write((f"Complete! Doubled number is: {numberx2}").encode())


# Запускаем HTTP сервер
server = HTTPServer(('0.0.0.0', 8081), ServiceHandler)
server.serve_forever()

"""
from fastapi import FastAPI, APIRouter
from scripts.scanner import do_ping_sweep, sent_http_request

router = APIRouter()


@router.get("/scan")
def run_scan(ip: str, count: int):
    results_dct = {}
    for nhost in range(count):
        results_dct.update(do_ping_sweep(ip, nhost))
    return results_dct


@router.post("/sendhttp")
def run_send_http(target: str, method: str, header: str = None, header_value: str = None):
    hd = {header: header_value} if (header and header_value) else None
    return sent_http_request(target, method, hd)


app = FastAPI()
app.include_router(router)
"""