import socket


def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # enable address reuse to avoid 'Address already in use' errors on  restarts that arent hard resets
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"server listening on {host}:{port}")

    try:
        while True:
            # accept new connection and print client connection notification
            client_socket, client_address = server_socket.accept()
            print(f"\n Client connected from {client_address}")

            with client_socket:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        print(f" Client {client_address} disconnected.")
                        break

                    message = data.decode('utf-8')
                    print(f"Received from client: {message}")

                    # Respond with exact 'Server Echo: <message>' format
                    response = f"Server Echo: {message}"
                    client_socket.sendall(response.encode('utf-8'))
                    print(f"Sent response: {response}")

    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()