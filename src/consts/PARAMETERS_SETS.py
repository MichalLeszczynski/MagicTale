from src.gameplay.params import Params
from src.consts import PARAMETERS


# Starting parameters for player's character
CHARACTER_PARAMS = Params()
CHARACTER_PARAMS.add_param(PARAMETERS.HP)
CHARACTER_PARAMS.add_param(PARAMETERS.MP)
CHARACTER_PARAMS.add_param(PARAMETERS.ST)
CHARACTER_PARAMS.add_param(PARAMETERS.ATT)

# Minimal parameters set for every being
BASE_PARAMS = Params()
BASE_PARAMS.add_param(PARAMETERS.HP)
BASE_PARAMS.add_param(PARAMETERS.ATT)