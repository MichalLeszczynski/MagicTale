from dataclasses import dataclass
from typing import List, Optional
from rpg.bf_rpg.entities import Character, Skill, Param, Trait, Item
from rpg.bf_rpg.repositories import (
    ITraitRepository,
    ISkillRepository,
    IItemRepository,
    IParamRepository,
    ICharacterRepository,
)


@dataclass
class GameLogic:
    characters: ICharacterRepository
    items: IItemRepository
    traits: ITraitRepository
    skills: ISkillRepository
    params: IParamRepository

    def add_item(self, character_id, item_id):
        character: Character = self.characters.get(character_id)
        item: Item = self.items.get(item_id)
        inventory: List[Item] = character.items
        inventory.append(item)

    def create_new_character(self, name="NoNameCharacter"):
        character = self.characters.create(name=name)
        return character

    def create_new_item(
        self, name="NoNameItem", value=0, weight=0, traits: Optional[List[Trait]] = None
    ) -> Item:
        item = self.items.create(name=name, value=value, weight=weight, traits=traits)
        return item

    def create_new_trait(
        self, name="NoNameTrait", affected_params=None, gained_skills=None
    ) -> Trait:
        trait = self.traits.create(
            name=name, affected_params=affected_params, gained_skills=gained_skills
        )
        return trait

    def create_new_skill(self, name="NoNameSkill", description="") -> Skill:
        skill = self.skills.create(name=name, description=description)
        return skill

    def create_new_param(self, name="NoNameParam", max_value=0) -> Param:
        param = self.params.create(name=name, max_value=max_value)
        return param
