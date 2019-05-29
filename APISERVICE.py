from abc import ABC, abstractmethod

class APISERVICE(ABC):
    @abstractmethod
    def buscarNombre(self, drinkName):
        # Regresa un objeto tipo dirnk :)
        pass