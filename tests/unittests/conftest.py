from ram_db.bf_ram_db.character import CharacterRepositories
from ram_db.bf_ram_db.item import ItemRepositories
from ram_db.bf_ram_db.param import ParamRepositories
from ram_db.bf_ram_db.skill import SkillRepositories
from ram_db.bf_ram_db.trait import TraitRepositories

STATIC_REPOSITORIES = [
    CharacterRepositories(),
    ItemRepositories(),
    TraitRepositories(),
    SkillRepositories(),
    ParamRepositories(),
]
