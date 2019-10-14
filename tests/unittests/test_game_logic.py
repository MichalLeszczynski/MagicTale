from rpg.bf_rpg.logic import GameLogic

from tests.unittests.conftest import STATIC_REPOSITORIES


def test_create_character_by_game_logic() -> None:

    logic = GameLogic(*STATIC_REPOSITORIES)
    character = logic.character_logic.create_new_character("Test Character")

    assert logic.character_logic.characters.get(character.id) == character
    assert character.name == "Test Character"


def test_create_item_by_game_logic() -> None:

    logic = GameLogic(*STATIC_REPOSITORIES)
    item = logic.item_logic.create_new_item("Test Item")

    assert logic.item_logic.items.get(item.id) == item
    assert item.name == "Test Item"


def test_create_trait_by_game_logic() -> None:
    logic = GameLogic(*STATIC_REPOSITORIES)
    trait = logic.trait_logic.create_new_trait("Test Trait")

    assert logic.trait_logic.traits.get(trait.id) == trait
    assert trait.name == "Test Trait"


# def test_adding_items_to_character_increase_params() -> None:
#
#     logic = GameLogic(*STATIC_REPOSITORIES)
#     character = logic.character_logic.create_new_character("Test Character")
#     trait1 = logic.trait_logic.create_new_trait(name="Test Trait 1", affected_params={"HP", 20})
#     trait2 = logic.trait_logic.create_new_trait(name="Test Trait 2", affected_params={"MP", -40})
#
#     item = logic.item_logic.create_new_item("Test Item", traits=[trait1, trait2])
#
#     character.add_item(item)
