import socket
import threading
import uuid

class TicTacToeServer:
    def __init__(self):
        self.host = "0.0.0.0"  # Listen on all available network interfaces
        self.port = 12345
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []
        self.games = {}  # Dictionary to manage game sessions

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)  # Allow multiple players and games
        print("Server is waiting for connections...")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connected to {client_address}")
            self.connections.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        # Handle game creation or joining here based on client messages
        client_socket.send("Enter 'JOIN game_id' to join an existing game or 'CREATE' to create a new game.".encode())
        data = client_socket.recv(1024).decode()
        
        if data.startswith("CREATE"):
            # Create a new game session
            game_id = uuid.uuid4().hex[:6].upper()
            self.games[game_id] = {"players": [client_socket], "board": None}
            client_socket.send(f"Game {game_id} created. You are player 1.".encode())
        elif data.startswith("JOIN"):
            # Extract the game_id and join an existing game
            _, game_id = data.split()
            if game_id in self.games and len(self.games[game_id]["players"]) < 2:
                self.games[game_id]["players"].append(client_socket)
                client_socket.send(f"Joined game {game_id} as player 2.".encode())
                # Initialize the game board here if needed
            else:
                client_socket.send("Invalid game ID or the game is full.".encode())
        else:
            client_socket.send("Invalid command. Enter 'JOIN game_id' or 'CREATE game_id'.".encode())

        # Handle game logic (moves, updates) within this game session
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            # Handle incoming messages for game moves, restart requests, etc.
            # Update the game state accordingly and send updates to the clients.

        # Clean up when a client disconnects or the game ends
        client_socket.close()

if __name__ == "__main__":
    server = TicTacToeServer()
    server.start()
