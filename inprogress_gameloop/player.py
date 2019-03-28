class player:
    def __init__(self,name):
        self.name = name
        self.event = None
    def change_event(self, new_event):
        self.event = new_event
    def exit_event(self):
        self.event = None
    def in_event(self):
        return self.event is None
