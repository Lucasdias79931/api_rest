from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Iterable

T = TypeVar("T")
ID = TypeVar("ID")


class Repository(ABC, Generic[T, ID]):

    @abstractmethod
    def save(self, entity: T) -> None:
        """
        This method must be implemented to persist an entity in the database.
        """
        ...

    @abstractmethod
    def get_by_id(self, entity_id: ID) -> T | None:
        """
        This method must be implemented to load an entity by id from the database.
        """
        ...

    @abstractmethod
    def get_all(self) -> Iterable[T]:
        """
        This method must be implemented to load all entities from the database.
        """
        ...

    @abstractmethod
    def update(self, entity: T) -> None:
        """
        This method must be implemented to update an entity in the database.
        """
        ...

    @abstractmethod
    def delete_or_mark_inactive(self, entity_id: ID) -> None:
        """
        This method must be implemented to delete or mark an entity as inactive in the database.
        """
        ...
