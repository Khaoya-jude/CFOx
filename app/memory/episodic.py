class InMemoryEpisodicMemory:
    def __init__(self):
        self.events = []

    def remember(self, event: dict):
        self.events.append(event)

    def recall(self, query: dict):
        return self.events
