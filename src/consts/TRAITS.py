from src.gameplay.trait import Trait
from src.consts import PARAMETERS

sharp = Trait("Sharp", {PARAMETERS.ST: 20, PARAMETERS.ATT: 5})
magical = Trait("Magical", {PARAMETERS.MP: 20})
poisoned = Trait("Poisoned", {PARAMETERS.ATT: 5, PARAMETERS.HP: -30})