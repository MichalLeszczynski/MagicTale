class Tile:
    def __init__(self, title="", description="", on_click=None):
        self.title = title
        self.description = description
        self.content = "{} \n \t {}".format(title, description)
        self.on_click = on_click

    def get_content(self):
        return self.content

    def execute(self, context=None):
        self.on_click(context)
