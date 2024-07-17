from cryptography.fernet import Fernet
import socket
import json
import base64

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            action = input("Enter action (put/get, type 'exit' to quit): ").strip()
            if action.lower() == 'exit':
                break
            elif action == 'put':
                key = input("Enter key: ").strip()
                message = input("Enter message: ").strip()
                message_bytes = message.encode('utf-8')  # Convert the message to bytes

                encripted_message = cipher_suite.encrypt(message_bytes)
                data = {
                    "put": (key, encripted_message.decode('utf-8'))
                }
                json_data = json.dumps(data).encode('utf-8')
                s.sendall(json_data)

            elif action == 'get':
                key = input("Enter key: ").strip()
                data = {
                    "get": key
                }
                json_data = json.dumps(data).encode('utf-8')
                s.sendall(json_data)
            else:
                print("Invalid action. Please enter 'put' or 'get'.")
                continue

            response_data = s.recv(1024)
            if not response_data:
                break

            response = response_data.decode('utf-8')

            if action == 'get':
                if response == "No such key":
                    print(f"{response}")
                else:
                    print(f"Received from server: {response}")
                    try:
                        decrypted_message = cipher_suite.decrypt(response_data.decode('utf-8'))
                        print(f"Decrypted message: {decrypted_message.decode('utf-8')}")
                    except Exception as e:
                        print(f"Error decrypting message: {e}")


if __name__ == "__main__":
    start_client()