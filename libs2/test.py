import time 
from threading import Thread

class Test:

    # def __init__(self):
    #     t = Thread(target = self.call)
    #     t.start()

    def call(self):        
        while True:
            print("test")
            time.sleep(0.5)