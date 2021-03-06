import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10002))
sock.listen(socket.SOMAXCONN)
conn, addr = sock.accept()

with open("skorogovorka_new.txt", "a", encoding="utf-8") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            print("Нет входящих данных")
            break
        f.write(f"{datetime.now()} {data.decode('utf - 8')}")

conn.close()
sock.close()
