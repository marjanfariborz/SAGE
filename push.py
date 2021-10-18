
class Push():
    def __init__(self, op = sum ):
        self.op = op
        self.localQ = []
        self.globalQ = []

    def recv_update(self, vid, value, weight):
        '''
        interface to reduce
        '''
        self.value = value
        self.weight = weight
        self.push(self)

    def send_update(self):
        '''
        based on the vid it either sends the futur work
        locally or globally
        I think it needs to be seperated

        if local:
            self.localQ.pop(0)
        else:
            self.globalQ.pop(0)
        '''
    def push(self):
        '''
        Performs push operation and calls send update and based on
        vid they need to store in local/globalQ
        '''


