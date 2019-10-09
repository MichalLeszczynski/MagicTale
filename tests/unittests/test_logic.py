from rpg.bf_rpg.logic import (
    CharacterLogic,
    ItemLogic,
    ParamLogic,
    SkillLogic,
    TraitLogic,
)

from ram_db.bf_ram_db.character import CharacterRepositories
from ram_db.bf_ram_db.item import ItemRepositories
from ram_db.bf_ram_db.param import ParamRepositories
from ram_db.bf_ram_db.skill import SkillRepositories
from ram_db.bf_ram_db.trait import TraitRepositories


def test_create_character() -> None:

    logic = CharacterLogic(CharacterRepositories())
    character = logic.create_new_character("Test Character")

    assert logic.characters.get(character.id) == character
    assert character.name == "Test Character"


def test_create_item() -> None:

    logic = ItemLogic(ItemRepositories())
    item = logic.create_new_item(name="Test Item")

    assert logic.items.get(item.id) == item
    assert item.name == "Test Item"


def test_create_param() -> None:

    logic = ParamLogic(ParamRepositories())
    param = logic.create_new_param(name="Test Param")

    assert logic.params.get(param.id) == param
    assert param.name == "Test Param"


def test_create_skill() -> None:
    logic = SkillLogic(SkillRepositories())
    skill = logic.create_new_skill(name="Test Skill")

    assert logic.skills.get(skill.id) == skill
    assert skill.name == "Test Skill"


def test_create_trait() -> None:
    logic = TraitLogic(TraitRepositories())
    trait = logic.create_new_trait(name="Test Trait")

    assert logic.traits.get(trait.id) == trait
    assert trait.name == "Test Trait"
