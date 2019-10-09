from typing import Optional, Dict, List

from rpg.bf_rpg.entities import Param, Skill, Trait
from rpg.bf_rpg.repositories import ITraitRepository
from ram_db.bf_ram_db.entity import EntityRepositories


class TraitRepositories(ITraitRepository, EntityRepositories[Trait]):
    def create(
        self,
        name: str,
        affected_params: Optional[Dict[Param, int]] = None,
        gained_skills: Optional[List[Skill]] = None,
    ) -> Trait:
        trait_id = self._ram_storage.next_pk()

        self._ram_storage.add(
            Trait(
                id=trait_id,
                name=name,
                affected_params=affected_params,
                gained_skills=gained_skills,
            )
        )

        return self._ram_storage.get(trait_id)
