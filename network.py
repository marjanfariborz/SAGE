class Network():
    def __init__(self):
        self.queue = []
        self.mpus = []

    def recv_updates(self, updates):
        for update in updates:
            vid = update.get_vid()
            for i in range(len(self.mpus)):
                if self.mpus[i].has_vertex(vid):
                    self.mpus[i].recv_update(update)

    def set_mpus(self, mpus):
        self.mpus = mpus
