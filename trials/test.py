import sys

sys.path.append("../")

from imports import *

if __name__ == "__main__":
    sharp = Trait("Sharp", {PARAMS.get_param("ST"): 20, PARAMS.get_param("ATT"): 5})
    magical = Trait("Magical", {PARAMS.get_param("MP"): 20})
    poisoned = Trait("Poisoned", {PARAMS.get_param("ATT"): 5, PARAMS.get_param("HP"): -30})
    test_traits = Traits(sharp, magical, poisoned)
    spear = Item(name="spear", weight=2, value=30, traits=test_traits)
    spear.print_full_item()
    
    print("\n\n")
    my_character = Character.create_new_character("Michal", "warrior")
    my_character.inventory.add_item(spear)

    my_character.inventory.display_precisely_inventory()
    print("\n\n*********\n")
    my_character.inventory.display_inventory()
    print("\n\n*********\n")

    my_character.params = copy.deepcopy(PARAMS)
    my_character.params.print()
    print("\n\n*********\n")

    my_character.inventory.apply_items(my_character)
    my_character.params.print()
    print("\n\n*********\n")

    my_character.params.reset_current_params()
    my_character.params.print()
    print("\n\n*********\n")

    enemy = Character.create_new_character("Rat", "archer")
    enemy.params = copy.deepcopy(BASE_PARAMS)
    enemy.params.print()
    enemy.params.update_param("Rage", 50)
    enemy.params.print()
    enemy.params.params["Rage"].current_value -= 50
    enemy.params.print()
