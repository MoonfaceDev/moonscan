from abc import abstractmethod, ABC
from typing import List


class BasePortListProvider(ABC):
    @abstractmethod
    def get_list(self, number_of_ports: int) -> List[int]:
        raise NotImplementedError()
