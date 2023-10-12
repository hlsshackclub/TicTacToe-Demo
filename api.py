import socket

class API():
    def connect(self):
        # Connect to the server
        self.server_host = "127.0.0.1"  # Replace with the server IP
        self.server_port = 12345
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_host, self.server_port))
        
    def sendMesg(self, mesg):
        self.client_socket.send(mesg.encode())
        
    def recvMesg(self):
        return self.client_socket.recv(1024).decode()