from abc import ABC, abstractmethod

class Card(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_action(self):
        pass
