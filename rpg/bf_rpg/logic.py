from dataclasses import dataclass
from typing import List, Optional, Tuple
from rpg.bf_rpg.entities import Character, Skill, Param, Trait, Item
from rpg.bf_rpg.repositories import ITraitRepository, ISkillRepository, IItemRepository, IParamRepository, ICharacterRepository, IEntityRepository


@dataclass
class CharacterLogic:
    characters: ICharacterRepository

    def create_new_character(self, name="NoNameCharacter"):
        character = self.characters.create(name)
        return character

    def apply_items(self, character: Character):
        pass

    def add_trait(self, character):
        pass

    def add_param(self):
        pass

    def add_item(self):
        pass

    def add_skill(self):
        pass


@dataclass
class ItemLogic:
    items: IItemRepository

    def create_new_item(self, name="NoNameItem", value=0, weight=0) -> Item:
        item = self.items.create(name=name, value=value, weight=weight)
        return item


@dataclass
class ParamLogic:
    params: IParamRepository

    def create_new_param(self, name="NoNameParam", value=0) -> Param:
        param = self.params.create(name=name, value=value)
        return param


@dataclass
class TraitLogic:
    traits: ITraitRepository

    def create_new_trait(self, name="NoNameTrait", description="") -> Trait:
        trait = self.traits.create(name=name)
        return trait


@dataclass
class SkillLogic:
    skills: ISkillRepository

    def create_new_skill(self, name="NoNameSkill", description="") -> Skill:
        skill = self.skills.create(name=name, description=description)
        return skill
