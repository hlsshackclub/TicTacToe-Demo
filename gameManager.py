import threading

class GameManager:
    def __init__(self, board, api):
        self.board = board
        self.api = api
    
    def check_for_messages(self):
        while True:
            data = self.api.recvMesg()
            if not data:
                break
            if (data.startswith("MOVE")):
                _, x, y = data.split()
                self.move(int(x), int(y))
                        
    def move(self, x, y):
        self.board.buttons[((y)*3)+x].update("other")
        
    def start(self):
        self.messageThread = threading.Thread(target = self.check_for_messages)
        self.messageThread.start()