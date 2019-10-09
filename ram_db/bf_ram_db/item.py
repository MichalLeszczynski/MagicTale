from typing import Optional, List

from rpg.bf_rpg.entities import Item, Trait
from rpg.bf_rpg.repositories import IItemRepository
from ram_db.bf_ram_db.entity import EntityRepositories


class ItemRepositories(IItemRepository, EntityRepositories[Item]):
    def create(
        self, name: str, value: int, weight: int, traits: Optional[List[Trait]] = None
    ) -> Item:
        item_id = self._ram_storage.next_pk()

        self._ram_storage.add(
            Item(id=item_id, name=name, value=value, weight=weight, traits=traits)
        )

        return self._ram_storage.get(item_id)
