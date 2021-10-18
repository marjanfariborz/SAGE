
class Push():
    def __init__(self, id, op = sum):
        self.op = op
        self.localQ = []
        self.globalQ = []
        self.id = id

    def recv_update(self, vid, value, weight):
        '''
        interface to reduce
        '''
        self.value = value
        self.weight = weight
        self.vid = vid
        self.push(self)

    def send_update(self, vid, value):
        '''
        based on the vid it either sends the futur work
        locally or globally
        I think it needs to be seperated

        if local:
            self.localQ.pop(0)
        else:
            self.globalQ.pop(0)
        '''
        if (vid % 2) == id:
            self.localQ.append({vid, value})
        else:
            self.globalQ.append({vid, value})

    def push(self):
        '''
        Performs push operation and calls send update and based on
        vid they need to store in local/globalQ
        '''
        propagate = self.op
        new_value = propagate(self.value, self.weight)
        self.send_update(self.vid, new_value)


