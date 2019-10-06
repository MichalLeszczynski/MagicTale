import abc
from typing import TypeVar, Generic, Dict, List, Optional

from rpg.bf_rpg.entities import Character, Item, Trait, Skill, Param


EntityType = TypeVar("EntityType")


class IEntityRepository(abc.ABC, Generic[EntityType]):
    @abc.abstractmethod
    def get(self, skill_id: int) -> EntityType:
        pass

    @abc.abstractmethod
    def save(self, skill: EntityType) -> EntityType:
        pass

    @abc.abstractmethod
    def search(self, name: Optional[str] = None) -> List[EntityType]:
        pass


class IParamRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str, val: int) -> Param:
        pass


class ISkillRepository(abc.ABC):
    @abc.abstractmethod
    def create(
        self,
        name: str,
        description: str,
        self_effect: Optional[Dict[Param, int]] = None,
        enemy_effect: Optional[Dict[Param, int]] = None,
    ) -> Skill:
        pass


class ICharacterRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str) -> Character:
        pass


class IItemRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str) -> Item:
        pass


class ITraitRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str) -> Trait:
        pass
