class Maquina():

    def __init__(self):
        self.cpu = 0
        self.memo = 0
        self.disk = 0

    def set_cpu(self, value):
        self.cpu = value

    def set_disk(self, value):
        self.disk = value

    def set_memo(self, value):
        self.memo = value

    def get_cpu(self):
        return self.cpu

    def get_disk(self):
        return self.disk

    def get_memo(self):
        return self.memo

