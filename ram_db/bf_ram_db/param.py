from rpg.bf_rpg.entities import Param
from rpg.bf_rpg.repositories import IParamRepository
from ram_db.bf_ram_db.entity import EntityRepositories


class ParamRepositories(IParamRepository, EntityRepositories[Param]):
    def create(self, name: str, max_value: int) -> Param:
        param_id = self._ram_storage.next_pk()

        self._ram_storage.add(
            Param(id=param_id, name=name, max_value=max_value, current_value=max_value)
        )

        return self._ram_storage.get(param_id)


if __name__ == "__main__":
    repo = ParamRepositories()
    repo.create("HP", 100)
    repo.create("HP", 100)
    repo.create("MP", 100)
    print(repo._ram_storage.all())
    print(repo.search("HP"))
