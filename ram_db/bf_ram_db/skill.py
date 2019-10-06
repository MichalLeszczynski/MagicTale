from typing import Optional, Dict

from rpg.bf_rpg.entities import Param, Skill
from rpg.bf_rpg.repositories import ISkillRepository
from ram_db.bf_ram_db.entity import EntityRepositories


class SkillRepositories(ISkillRepository, EntityRepositories[Skill]):
    def create(
        self,
        name: str,
        description: str,
        self_effect: Optional[Dict[Param, int]] = None,
        enemy_effect: Optional[Dict[Param, int]] = None,
    ) -> Skill:
        skill_id = self._ram_storage.next_pk()

        self._ram_storage.add(
            Skill(
                id=skill_id,
                name=name,
                self_effect=self_effect,
                enemy_effect=enemy_effect,
            )
        )

        return self._ram_storage.get(skill_id)
