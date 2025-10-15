from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def load_data(self, source: str) -> None:
        pass

    @abstractmethod
    def process_data(self) -> Any:
        pass

    @abstractmethod
    def save_data(self, destination: str) -> None:
        pass