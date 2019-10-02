import abc
from rpg.bf_rpg.entities import Character, Item, Trait, Skill, Param
from typing import List, Dict


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


class ISkillRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str) -> Skill:
        pass


class IParamRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str) -> Param:
        pass
