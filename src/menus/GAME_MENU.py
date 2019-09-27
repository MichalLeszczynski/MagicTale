from src.menus.menu import Menu
from src.menus.tile import Tile
from src.events import GAME_EVENTS

t1 = Tile("Fight", "Choose to start a fight with a new enemy.", GAME_EVENTS.game_fight)
t2 = Tile("Inventory", "Choose to view your inventory.", GAME_EVENTS.game_inventory)
t3 = Tile("Exit", "Choose to exit this adventure.", GAME_EVENTS.game_exit)

game_menu = Menu(t1, t2, t3)

if __name__ == "__main__":
    game_menu.print()
