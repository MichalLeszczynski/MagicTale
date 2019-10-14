from typing import Optional, List

from rpg.bf_rpg.entities import Param, Skill, Trait, Character, Item
from rpg.bf_rpg.repositories import ICharacterRepository
from ram_db.bf_ram_db.entity import EntityRepositories


class CharacterRepositories(ICharacterRepository, EntityRepositories[Character]):
    def create(
        self,
        name: str,
        items: Optional[List[Item]] = [],
        traits: Optional[List[Trait]] = [],
        skills: Optional[List[Skill]] = [],
        params: Optional[List[Param]] = [],
    ) -> Character:
        character_id = self._ram_storage.next_pk()

        self._ram_storage.add(
            Character(
                id=character_id,
                name=name,
                items=items,
                traits=traits,
                skills=skills,
                params=params,
            )
        )

        return self._ram_storage.get(character_id)
