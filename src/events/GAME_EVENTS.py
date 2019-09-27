from src.events.event import Event


game_fight = Event(lambda context: print("I will be fighting!"))


game_inventory = Event(lambda context: context.player.inventory.display_inventory())


game_exit = Event(lambda context: exit())


