class Event:
    def __init__(self, action):
        self.action = action

    def __call__(self, context=None):
        self.action(context)
