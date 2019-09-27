from src.consts.PARAMETERS_SETS import CHARACTER_PARAMS, BASE_PARAMS
from src.gameplay.trait import Trait, Traits
from src.gameplay.item import Item
from src.gameplay.character import Character
import copy
from src.consts import ITEMS

if __name__ == "__main__":
    sharp = Trait(
        "Sharp",
        {CHARACTER_PARAMS.get_param("ST"): 20, CHARACTER_PARAMS.get_param("ATT"): 5},
    )
    magical = Trait("Magical", {CHARACTER_PARAMS.get_param("MP"): 20})
    poisoned = Trait(
        "Poisoned",
        {CHARACTER_PARAMS.get_param("ATT"): 5, CHARACTER_PARAMS.get_param("HP"): -30},
    )
    test_traits = Traits(sharp, magical, poisoned)

    ITEMS.spear.print_full_item()

    # print("\n\n")
    # my_character = Character("Michal")
    # my_character.inventory.add_item(spear)
    #
    # my_character.inventory.display_precisely_inventory()
    # print("\n\n*********\n")
    # my_character.inventory.display_inventory()
    # print("\n\n*********\n")
    #
    # my_character.params = copy.deepcopy(CHARACTER_PARAMS)
    # my_character.params.print()
    # print("\n\n*********\n")
    #
    # my_character.inventory.apply_items(my_character)
    # my_character.params.print()
    # print("\n\n*********\n")
    #
    # my_character.params.reset_current_params()
    # my_character.params.print()
    # print("\n\n*********\n")
    #
    # enemy = Character("Rat")
    # enemy.params = copy.deepcopy(BASE_PARAMS)
    # enemy.params.print()
    # enemy.params.update_param("Rage", 50)
    # enemy.params.print()
    # enemy.params.params["Rage"].current_value -= 50
    # enemy.params.print()
