""" TODO Documentation """

from src.gameplay.params import Param

"""
 affected_stats : dictionary : {param, value}
"""


class Trait:
    """ TODO Documentation """

    def __init__(self, name, affected_params={}):
        self.name = name
        self.affected_params = affected_params
        # print("TODO")

    def apply_params(self, being):
        for param in self.affected_params:
            being.params.update_param(param.name, self.affected_params[param])


class Traits:
    def __init__(self, *init_traits):
        self.traits = init_traits

    def add_trait(self, trait):
        self.traits.append(trait)

    def print(self):
        print("Traits: ", end=" ")
        for trait in self.traits:
            print("< {} >".format(trait.name), end=" ")
        print("")

    def apply_traits(self, being):
        for trait in self.traits:
            trait.apply_params(being)

