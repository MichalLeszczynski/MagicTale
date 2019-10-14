from dataclasses import dataclass
from typing import List, Optional, Tuple
from rpg.bf_rpg.entities import Character, Skill, Param, Trait, Item
from rpg.bf_rpg.repositories import (
    ITraitRepository,
    ISkillRepository,
    IItemRepository,
    IParamRepository,
    ICharacterRepository,
)


@dataclass
class CharacterLogic:
    characters: ICharacterRepository

    def create_new_character(self, name="NoNameCharacter"):
        character = self.characters.create(name=name)
        return character

    def apply_items(self, character: Character):
        pass

    def add_trait(self):
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

    def create_new_item(
        self, name="NoNameItem", value=0, weight=0, traits: Optional[List[Trait]] = None
    ) -> Item:
        item = self.items.create(name=name, value=value, weight=weight, traits=traits)
        return item


@dataclass
class TraitLogic:
    traits: ITraitRepository

    def create_new_trait(self, name="NoNameTrait") -> Trait:
        trait = self.traits.create(name=name)
        return trait


@dataclass
class SkillLogic:
    skills: ISkillRepository

    def create_new_skill(self, name="NoNameSkill", description="") -> Skill:
        skill = self.skills.create(name=name, description=description)
        return skill


@dataclass
class ParamLogic:
    params: IParamRepository

    def create_new_param(self, name="NoNameParam", value=0) -> Param:
        param = self.params.create(name=name, value=value)
        return param


class GameLogic:
    def __init__(
        self,
        characters: ICharacterRepository,
        items: IItemRepository,
        traits: ITraitRepository,
        skills: ISkillRepository,
        params: IParamRepository,
    ):
        self.character_logic = CharacterLogic(characters)
        self.item_logic = ItemLogic(items)
        self.trait_logic = TraitLogic(traits)
        self.skill_logic = SkillLogic(skills)
        self.param_logic = ParamLogic(params)
