from src.imports import *
from src.menus import MAIN_MENU


class Context:
    def __init__(self):
        self.player = None

    def create_new_character(self, name=""):
        if not name:
            name = input("Your name: ")
        self.player = Character(name)

    def new_game(self):
        MAIN_MENU.main_menu.invoke(self)

    def save_game(self):
        pass

    def load_game(self, file):
        pass

    def get_player(self):
        return self.player
