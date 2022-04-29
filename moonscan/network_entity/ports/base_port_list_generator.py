from abc import abstractmethod, ABC
from typing import List


class BasePortListGenerator(ABC):
    @abstractmethod
    def generate(self, number_of_ports: int) -> List[int]:
        raise NotImplementedError()
