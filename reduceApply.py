from graph_reader import Vertex

class Apply():
    def __init__(self, id, op = sum):
        self.id = id
        self.op = op
    def arbitrate(self):
        '''
        arbitarte in its local worklist
        finds a vid in worklist with valid =1
        self.vtemp = vtemp
        self.value = value
        '''

    def reduce(self):
        op = self.op