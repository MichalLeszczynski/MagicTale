from imports import *

if __name__=="__main__":
    sharp = Trait("Sharp", {BASE_PARAMS.get_param("ST"): 20, BASE_PARAMS.get_param("ATT"): 5})
    magical = Trait("Magical", {BASE_PARAMS.get_param("MP"): 20})
    test_traits = Traits(sharp, magical)
    spear = Item(name="spear", weight=2, value=30, traits=test_traits)
    # spear.print_full_item()

    my_character = Character.create_new_character("Michal", "warrior")
    my_character.inventory.add_item(spear)
    my_character.inventory.display_inventory()
    my_character.params = copy.deepcopy(BASE_PARAMS)
    my_character.params.print()
    my_character.inventory.apply_items(my_character)
    my_character.params.print()
    # my_character.params.reset_current_params()
    my_character.params.print()

    enemy = Character.create_new_character("Rat", "archer")
    enemy.params = copy.deepcopy(BASE_PARAMS)
    enemy.params.print()
    enemy.params.update_param("Rage", 50)
    enemy.params.print()

