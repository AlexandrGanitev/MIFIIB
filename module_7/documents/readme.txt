Создание файла requirement.txt:
$ pip freeze > requirement.txt

Dockerfile:
FROM python:3.9
WORKDIR /code
LABEL Author=A.Ganitev
LABEL module=7.10
COPY ./requirements.txt /code/requirements.txt
# folder /code belongs to the inner structure of this Docker container
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /code/app
EXPOSE 3009
ENTRYPOINT ["python3"]
CMD ["app/main.py"]
# CMD ["app/main.py", "--host", "0.0.0.0", "--port", "3009"] # здесь надо было именно через / указать путь до main.py
# во вложенной директории app

Создание Docker image:
$ module_7 % docker build -t api_scaner .
# Запуск: docker run api_scaner
Запуск с привязкой порта: docker run -p 3009:3009 api_scaner

Note: Also make sure your process is listening on host 0.0.0.0 (instead of localhost).
Container's localhost is not the same as your host's localhost

# Обновление, надо убрать доп.символы в переменной Temp:ValueError: invalid literal for int() with base 10: '115\\n'
# Запуск Debagger-а для такой программы с API:
# 1. Отмечаем breakpoints, запускаем дебаггер
# 2. В Postman отправляем запрос и смотрим в окне дебаггера...

        # пришлосъ пойти на такую хитрость с replace(), терерь сканер работает! Символ '\\n' был удалён из 4-го октета.
        ip_parts[3] = ip_parts[3].replace('\\n', '')
        print(ip_parts[3])
        network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
        ping = "ping -c 1 "
        time1 = datetime.datetime.now()
        # for ip in range(115, 118) :  # так отрабатывает, ниже вариант даёт ошибку:
            #     for ip in range(int(ip_parts[3]), int(ip_parts[3])+int(5)) :
            #                     ^^^^^^^^^^^^^^^^
            # ValueError: invalid literal for int() with base 10: '1\\n\\n'
            # проблема связана со строкой выше: content = self.rfile.read(length), где добаляюся символы 'b', \n.
            # надо их удалить, работаю...


*******************************************************************
# Documentation: https://docs.python.org/3/library/http.server.html
# вызвал сервер командой:
# python -m http.server
# ответ:
# Serving HTTP on :: port 8000 (http://[::]:8000/) ...
# надо разобраться, как передавать GET запрос через Postman. Оригинальная программа работала так:
# python3 main_start.py scan -i 192.168.1.1 -n 10
# ---------> Работает вариант SCAN!!!
# запустил скрипт, стартовал сервер, вывод виден в терминале и Postman выдаёт разультат.
# вот только он сканирует закодированный адрес и число хостов: ping_list = do_ping_sweep("192.168.1.115", 2), а
# хотелось бы передавать в запросе GET. Разбираюсь.

"""
$ python3 main.py
127.0.0.1 - - [12/Mar/2023 23:56:45] "GET /?ip=192.168.1.115&num_scanned_hosts=5 HTTP/1.1" 200 -
192.168.1.115

**********************************************************************

Full output of ping:  ['PING 192.168.1.115 (192.168.1.115): 56 data bytes\n', '\n', '--- 192.168.1.115 ping statistics ---\n', '1 packets transmitted, 0 packets received, 100.0% packet loss\n']
[#] Result of scanning 192.168.1.115
PING 192.168.1.115 (192.168.1.115): 56 data bytes

--- 192.168.1.115 ping statistics ---

1 packets transmitted, 0 packets received, 100.0% packet loss


This IP doesn't belong to the network

**********************************************************************

**********************************************************************

Full output of ping:  ['PING 192.168.1.116 (192.168.1.116): 56 data bytes\n', '64 bytes from 192.168.1.116: icmp_seq=0 ttl=64 time=2.363 ms\n', '\n', '--- 192.168.1.116 ping statistics ---\n', '1 packets transmitted, 1 packets received, 0.0% packet loss\n', 'round-trip min/avg/max/stddev = 2.363/2.363/2.363/0.000 ms\n']
[#] Result of scanning 192.168.1.116
PING 192.168.1.116 (192.168.1.116): 56 data bytes



--- 192.168.1.116 ping statistics ---


This IP belongs to the network

**********************************************************************
['192.168.1.116']

"""




