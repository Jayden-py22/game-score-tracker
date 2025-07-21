import socket
import json

print("Connecting to server...")

HOST = '127.0.0.1'
PORT = 65432

def send_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(request).encode())
        response = s.recv(4096)
        try:
            print("Response:", json.loads(response.decode()))
        except:
            print("Response:", response.decode())

if __name__ == "__main__":
    # Example usage:
    send_request({"action": "add-score", "name": "Alice", "score": 150, "date": "2025-05-12"})
    send_request({"action": "list-scores"})
    input("Press Enter to exit...")