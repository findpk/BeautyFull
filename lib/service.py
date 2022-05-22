import manager
import uuid

class Service:
    def __init__(self):
        self.manager = manager.Manager()

    def createCart(self):
        id = str(uuid.uuid4())
        return self.manager.createCart(id)
