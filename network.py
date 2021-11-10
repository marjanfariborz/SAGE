class Network():
    def __init__(self, debug_print=False):
        self.queue = []
        self.mpus = []
        self.active = False
        self.name = "Network"
        self.debug_print = debug_print

    def get_name(self):
        return self.name

    def print_debug(self, debug):
        if self.debug_print:
            print(f"{self.name}: {debug}")

    def recv_updates(self, updates):
        self.print_debug(f"Received updates.\nupdates: {updates}")
        self.print_debug(f"Added updates to the queue.\nqueue: {self.queue}")
        self.queue = self.queue + updates
        if not self.active:
            self.print_debug(f"Network: Activating.")
            self.active = True
            while len(self.queue) != 0:
                self.print_debug("Network: Sending updates from the queue.")
                update = self.queue.pop(0)
                self.print_debug(f"Update picked from the top of queue {update}.")
                vid = update.get_vid()
                self.print_debug(f"Update is to vid {vid}.")
                for i in range(len(self.mpus)):
                    if self.mpus[i].has_vertex(vid):
                        self.print_debug(f"Found vid {vid} in MPU{i}.")
                        self.print_debug(f"Sending the update to MPU{i}")
                        self.mpus[i].recv_update(update)
            self.print_debug("Emptied the queue. Deactivating.")
            self.active = False
            solutions = []
            vertex_stats = []
            for mpu in self.mpus:
                solutions = solutions + mpu.get_solutions()
                vertex_stats += mpu.get_vertex_stats()

            print(f"Printing the current solutions.\nsolutions: {solutions}")
            print(f"Printing the vertex stats.\n VertexStats: {vertex_stats}")

    def send_initial_update(self, update):
        self.print_debug("Sending the first update to start the algorithm.")
        self.print_debug(f"Initial update: {update}")
        vid = update.get_vid()
        for i in range(len(self.mpus)):
            if self.mpus[i].has_vertex(vid):
                self.print_debug(f"Found vid {vid} in MPU{i}.")
                self.print_debug(f"Sending the update to MPU{i}")
                self.mpus[i].recv_update(update)

    def set_mpus(self, mpus):
        self.mpus = mpus
