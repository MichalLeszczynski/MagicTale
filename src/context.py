from src.imports import *


class Context:

    @staticmethod
    def create_new_character(name=""):
        if not name:
            name = input("Your name: ")
        return Character(name)