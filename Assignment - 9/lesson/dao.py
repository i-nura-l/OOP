from abc import ABC, abstractmethod

class AbstractDao(ABC):
    @abstractmethod
    def get_by_id(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
class PersonDao(AbstractDao):
    def get_by_id(self):
        pass

    def get_all(self):
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
