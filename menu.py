class Menu:
    def __init__(self, *tiles):
        self.tiles = tiles

    def print(self):
        for index, tile in enumerate(self.tiles):
            print("{}. {}".format(index + 1, tile.content))

    def add_tile(self, tile):
        self.tiles.append(tile)

    def invoke(self):
        self.print()
        self.take_input()

    def take_input(self, message):
        return input(message)


class Tile:
    def __init__(self, title="", description="", on_click=None):
        self.content = "{} \n \t {}".format(title, description)
        self.on_click = on_click

    def get_content(self):
        return self.content

    def execute(self):
        self.on_click()


if __name__ == "__main__":
    pass
