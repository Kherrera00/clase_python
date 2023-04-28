from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class concretesStrategy1(Strategy):
    def method1(self):
        #Implementacion del metodo que corresponde a la estrategia 1
        pass

class ConcretesStrategy2(Strategy):
    def method2(self):
        pass

class Context():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = Strategy
    
    #Get

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    #Set

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def entryPoint(self) -> None:

        self.strategy.method1();

#metodo principal del modulo:

if __name__ == "_main_":

    estrategia = input("Elija la estrategia a usar (1,2)")

    if estrategia == "1":
        context = Context(concretesStrategy1())
    else: 
        context = Context(ConcretesStrategy2())
    
    context.entryPoint()
    
