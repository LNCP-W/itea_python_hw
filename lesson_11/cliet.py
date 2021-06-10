import socket

with open("skorogovorka.txt", "w", encoding="utf-8") as f:
    f.write("""В недрах тундры
Выдры в гетрах
Тырят в вёдра
Ядра кедров!

Выдрав с выдры
В тундре гетры
Вытру выдрой ядра кедров
Вытру гетрой выдре морду
Ядра в вёдра
Выдру в тундру!""")

sock = socket.create_connection(("127.0.0.1", 10002))

with open("skorogovorka.txt", "r", encoding="utf-8") as f:
    x = f.readline()
    while x != "":
        sock.send(x.encode("utf-8"))
        x = f.readline()

sock.close()
