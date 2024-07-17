import socket
import json

encrypted_db = {}

def put(key, enc_value):
    encrypted_db[key] = enc_value



def get(key):
    if key not in encrypted_db.keys():
        return "No such key"
    return encrypted_db[key]


def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server started. Listening on {host}:{port}")

        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if "put" in data.decode('utf-8'):
                    key, enc_value = json.loads(data.decode('utf-8'))["put"]
                    put(key, enc_value)
                    conn.sendall(b"Successfully added ket: value to the DB")
                elif "get" in data.decode('utf-8'):
                    key = json.loads(data.decode('utf-8'))["get"]
                    enc_value = get(key)
                    conn.sendall(enc_value.encode('utf-8'))



if __name__ == "__main__":
    start_server()