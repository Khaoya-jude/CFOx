from abc import ABC, abstractmethod


class Memory(ABC):
    @abstractmethod
    def remember(self, event: dict):
        pass

    @abstractmethod
    def recall(self, query: dict):
        pass
