from src.menus import GAME_MENU
from src.events.event import Event


main_new_game = Event(lambda _: GAME_MENU.game_menu.invoke())


main_credits = Event(lambda _: print("Game made by Michal Leszczynski. TY!"))


main_exit = Event(lambda context: exit())
