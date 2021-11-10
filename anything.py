class Anything():
    def __init__(self, owner, aid, debug_print):
        self.owner = owner
        self.id = aid
        self.debug_print = debug_print
        self.name = ""

    def set_name(self):
        self.name = f"{self.owner.get_name()}.{self.__class__.__name__}{self.id}"

    def get_name(self):
        return self.name

    def print_debug(self, debug):
        if self.debug_print:
            print(f"{self.name}: {debug}")
