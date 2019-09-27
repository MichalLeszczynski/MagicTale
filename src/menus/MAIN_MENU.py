from src.menus.menu import Menu
from src.menus.tile import Tile
from src.events import MAIN_EVENTS

t1 = Tile(
    "New Game",
    "Choose to start a new game with a new character.",
    MAIN_EVENTS.main_new_game,
)
t2 = Tile(
    "Credits", "Choose to view credits and inspirations.", MAIN_EVENTS.main_credits
)
t3 = Tile("Exit", "Choose to exit this game.", MAIN_EVENTS.main_exit)

main_menu = Menu(t1, t2, t3)

if __name__ == "__main__":
    main_menu.print()
