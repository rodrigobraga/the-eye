from __future__ import annotations

from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class Validator(ABC):
    """Base class for all validators."""

    def __init__(self, category: str, name: str) -> None:
        self.category = category
        self.name = name

    @abstractmethod
    def validate(self, raw: dict) -> bool:
        pass


class Creator(ABC):
    """Base class for all creators."""

    @abstractmethod
    def factory(self) -> Validator:
        pass
