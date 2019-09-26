from menu import Menu, Tile
from events import game_events

t1 = Tile("Fight", "Choose to start a fight with a new enemy.", game_events.game_fight)
t2 = Tile("Inventory", "Choose to view your inventory.", game_events.game_inventory)
t3 = Tile("Exit", "Choose to exit this adventure.", game_events.game_exit)

game_menu = Menu(t1, t2, t3)

if __name__ == "__main__":
    game_menu.print()
