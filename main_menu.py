from menu import Menu, Tile
from events import main_events

t1 = Tile(
    "New Game",
    "Choose to start a new game with a new character.",
    main_events.main_new_game,
)
t2 = Tile(
    "Credits", "Choose to view credits and inspirations.", main_events.main_credits
)
t3 = Tile("Exit", "Choose to exit this game.", main_events.main_exit)

main_menu = Menu(t1, t2, t3)

if __name__ == "__main__":
    main_menu.print()
