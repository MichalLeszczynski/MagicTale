from typing import List, Optional, Tuple

import pytest

from rpg.bf_rpg.repositories import ICharacterRepository, IParamRepository, IItemRepository, ISkillRepository, ITraitRepository
from rpg.bf_rpg.entities import Character, Skill, Param, Trait, Item

StaticRepositories = Tuple[ICharacterRepository, IParamRepository, IItemRepository, ISkillRepository, ITraitRepository]


@pytest.fixture(scope="function")
def prepare_repositories() -> StaticRepositories:

    param = Param(id=1, name="HP", max_value=100, current_value=50)
    trait = Trait(id=1, name="sharp", affected_params={param: 30})
    item = Item(id=1, name="Spear", value=50, weight=3, traits=List[trait])
    character = Character(id=1, name="Michal")

    class Characters(ICharacterRepository):
        def save(self, _character: Character) -> Character:
            nonlocal character
            character = _character
            return character

        def create(self, client: Client) -> Order:
            ...

        def get(self, character_id: int) -> Order:
            return character

        def search(
            self, client: Optional[Client] = None, created: Optional[datetime] = None
        ) -> List[Order]:
            pass

    class Products(IProductRepository):
        def create(self, name: str, price: float) -> Product:
            ...

        def get(self, product_id: int) -> Product:
            return product

    class Clients(IClientRepository):
        def create(self, name: str) -> Client:
            ...

        def get(self, client_id: int) -> Client:
            ...

    return Orders(), Products(), Clients()
