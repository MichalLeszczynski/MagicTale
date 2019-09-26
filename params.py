""" TODO Documentation """

START_PARAMS_VALUE = 100
JUST_VALUE = 15


class Params:
    """ TODO Documentation """

    def __init__(self):
        """ TODO Documentation """
        print("Creating params!")
        self.params = {}

    def add_param(self, param):
        """ TODO Documentation """

        self.params[param.name] = param

    def reset_current_params(self):
        """ TODO Documentation """

        for key, param in self.params.items():
            param.reset()

    def print(self):
        """ TODO Documentation """

        print("")
        for key, param in self.params.items():
            param.print()
        print("")

    def get_param(self, name):
        return self.params[name]

    def update_param(self, name, value):
        self.params.setdefault(name, Param(name, 0))
        self.params[name].current_value += value


class Param:
    """ TODO Documentation """

    def __init__(self, name, max_value):
        """ TODO Documentation """

        self.name = name
        self.max_value = max_value
        self.current_value = self.max_value

    def print(self):
        """ TODO Documentation """
        if self.current_value == self.max_value:
            text = "{}: {}"
        else:
            text = "{}: {}/{}"
        print(
            text.format(self.name, self.current_value, self.max_value).ljust(
                JUST_VALUE
            ),
            end="",
        )

    def reset(self):
        """ TODO Documentation """

        self.current_value = self.max_value


if __name__ == "__main__":

    HP = Param("HP", 100)
    MP = Param("MP", 100)
    ST = Param("ST", 100)

    parameters = Params()

    parameters.add_param(HP)
    parameters.add_param(MP)
    parameters.add_param(ST)

    parameters.print()

    parameters.params["HP"].current_value -= 50

    parameters.print()

    parameters.reset_current_params()

    parameters.print()
