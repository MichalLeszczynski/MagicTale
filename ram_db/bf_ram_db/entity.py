from ram_db.bf_ram_db.ram_storage import RamStorage
from rpg.bf_rpg.repositories import IEntityRepository, EntityType
from typing import List, Optional


class EntityRepositories(IEntityRepository):
    def __init__(self, static_data: Optional[List[EntityType]] = None) -> None:
        self._ram_storage: RamStorage[EntityType] = RamStorage[EntityType]()

        if static_data is None:
            static_data = []

        for skill in static_data:
            self._ram_storage.add(skill)

    def get(self, skill_id: int) -> EntityType:
        result = self._ram_storage.get(skill_id)
        if result is None:
            raise Exception("EntityType of id: {} not found".format(skill_id))
        return result

    def save(self, skill: EntityType) -> EntityType:
        self._ram_storage.add(skill)
        return skill

    def search(self, name: Optional[str] = None) -> List[EntityType]:

        storage = self._ram_storage
        storage = storage.search(name=name)
        return storage.all()
