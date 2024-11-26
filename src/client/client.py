import socket

PORT = 4444

def client_connection(HOST, task, id, units):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            message = s.recv(4096).decode("utf-8")

            if message.startswith("Task_ID"):
                s.sendall(task.encode() + b"\n")

            elif message.startswith("Matrikelnummer"):
                s.sendall(id.encode() + b"\n")

                message = s.recv(4096).decode("utf-8")

                if message.startswith("Anzahl"):
                    s.sendall(units.encode() + b"\n")

                    message = s.recv(4096).decode("utf-8")

                    if "NOK" in message :
                        s.close()
                        return False
                    else:
                        s.close()
                        return True
                else:
                    items = message.split("\n")

                    rand = items[items.index("Zufallszahl Zx:") + 1]
                    seed = items[items.index("Startwert:") + 1]
                    poly = items[items.index("Polynomial:") + 1]

                    s.close()
                    return {"rand": rand, "seed": seed, "poly": poly.split("x^")}
        