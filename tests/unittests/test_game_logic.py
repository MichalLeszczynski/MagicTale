from rpg.bf_rpg.logic import GameLogic

from rpg.bf_rpg.entities import Param

from tests.unittests.conftest import STATIC_REPOSITORIES


def test_create_character_by_game_logic() -> None:

    logic = GameLogic(*STATIC_REPOSITORIES)
    character = logic.create_new_character("Test Character")

    assert logic.characters.get(character.id) == character
    assert character.name == "Test Character"


def test_create_item_by_game_logic() -> None:

    logic = GameLogic(*STATIC_REPOSITORIES)
    item = logic.create_new_item("Test Item")

    assert logic.items.get(item.id) == item
    assert item.name == "Test Item"


def test_create_trait_by_game_logic() -> None:
    logic = GameLogic(*STATIC_REPOSITORIES)
    trait = logic.create_new_trait("Test Trait")

    assert logic.traits.get(trait.id) == trait
    assert trait.name == "Test Trait"


def test_adding_items_to_character_increase_params() -> None:

    logic = GameLogic(*STATIC_REPOSITORIES)
    character = logic.create_new_character("Test Character")

    param1 = logic.create_new_param("HP", 100)
    param2 = logic.create_new_param("MP", 100)

    trait1 = logic.create_new_trait(name="Test Trait 1", affected_params={param1: 20})
    trait2 = logic.create_new_trait(name="Test Trait 2", affected_params={param2: -40})

    item = logic.create_new_item("Test Item", traits=[trait1, trait2])

    assert param1.id == 1
    assert param2.id == 2
    assert trait1.id == 1
    assert trait2.id == 2
    assert item.id == 1

    logic.add_item(character_id=1, item_id=1)

    assert logic.characters.get(1).items[0] == item == logic.items.get(1)
