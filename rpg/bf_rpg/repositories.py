import abc
from typing import TypeVar, Generic, Dict, List, Optional

from rpg.bf_rpg.entities import Character, Item, Trait, Skill, Param


EntityType = TypeVar("EntityType")


class IEntityRepository(abc.ABC, Generic[EntityType]):
    @abc.abstractmethod
    def get(self, entity_id: int) -> EntityType:
        pass

    @abc.abstractmethod
    def save(self, entity: EntityType) -> EntityType:
        pass

    @abc.abstractmethod
    def search(self, name: Optional[str] = None) -> List[EntityType]:
        pass


class IParamRepository(IEntityRepository):
    @abc.abstractmethod
    def create(self, name: str, value: int) -> Param:
        pass


class ISkillRepository(IEntityRepository):
    @abc.abstractmethod
    def create(
        self,
        name: str,
        description: str,
        self_effect: Optional[Dict[Param, int]] = None,
        enemy_effect: Optional[Dict[Param, int]] = None,
    ) -> Skill:
        pass


class ICharacterRepository(IEntityRepository):
    @abc.abstractmethod
    def create(
            self,
            name: str,
            items: Optional[List[Item]] = None,
            traits: Optional[List[Trait]] = None,
            skills: Optional[List[Skill]] = None,
            params: Optional[List[Param]] = None
    ) -> Character:
        pass


class IItemRepository(IEntityRepository):
    @abc.abstractmethod
    def create(
            self,
            name: str,
            value: int,
            weight: int,
            traits: Optional[List[Item]] = None,
    ) -> Item:
        pass


class ITraitRepository(IEntityRepository):
    @abc.abstractmethod
    def create(
            self,
            name: str,
            affected_params: Optional[Dict[Param, int]] = None,
            gained_skills: Optional[List[Skill]] = None,
    ) -> Trait:
        pass
