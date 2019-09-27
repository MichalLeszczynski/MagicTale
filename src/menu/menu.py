from src.menu.tile import Tile


class Menu:
    def __init__(self, *tiles):
        self.tiles = {}
        for tile in tiles:
            self.add_tile(tile)

    def print(self):
        print("\n\n")
        for index, (title, tile) in enumerate(self.tiles.items()):
            print("{}. {}".format(index + 1, tile.content))

    def add_tile(self, tile):
        self.tiles[tile.title] = tile

    def invoke(self):
        self.print()
        choice = input("\nYour choice: ")
        self.tiles[choice].on_click()


if __name__ == "__main__":
    pass
