from src.gameplay.item import Item
from src.gameplay.trait import Traits
from src.consts import TRAITS

spear = Item(name="spear", weight=2, value=30, traits=Traits(TRAITS.magical, TRAITS.sharp))
