from abc import abstractmethod, ABCMeta


class TestAction(metaclass=ABCMeta):
    def __init__(self,
                 sleep: int = 0):
        self.sleep = sleep

    @property
    @abstractmethod
    def action_type(self):
        pass
