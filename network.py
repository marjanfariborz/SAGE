class Network():
    def __init__(self):
        self.queue = []
        self.mpus = []
        self.active = False

    def recv_updates(self, updates):
        print(f"Network: Received updates.\nupdates: {updates}")
        print(f"Network: Added updates to the queue.\nqueue: {self.queue}")
        self.queue = self.queue + updates
        if not self.active:
            print(f"Network: Activating.")
            self.active = True
            while len(self.queue) != 0:
                print(f"Network: Sending updates from the queue.")
                update = self.queue.pop(0)
                print(f"Network: Update picked from the top of queue {update}.")
                vid = update.get_vid()
                print(f"Network: Update is to vid {vid}.")
                for i in range(len(self.mpus)):
                    if self.mpus[i].has_vertex(vid):
                        print(f"Network: Found vid {vid} in MPU{i}.")
                        print(f"Network: Sending the update to MPU{i}")
                        self.mpus[i].recv_update(update)
            print("Network: Emptied the queue. Deactivating.")
            self.active = False

    def send_initial_update(self, update):
        print(f"Network: Sending the first update to start the algorithm.")
        print(f"Network: Initial update: {update}")
        vid = update.get_vid()
        for i in range(len(self.mpus)):
            if self.mpus[i].has_vertex(vid):
                print(f"Network: Found vid {vid} in MPU{i}.")
                print(f"Network: Sending the update to MPU{i}")
                self.mpus[i].recv_update(update)

    def set_mpus(self, mpus):
        self.mpus = mpus
