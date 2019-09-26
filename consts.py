from params import Param, Params

HP = Param("HP", 100)
MP = Param("MP", 100)
ST = Param("ST", 100)
ATT = Param("ATT", 1)
BASE_PARAMS = Params()

BASE_PARAMS.add_param(HP)
BASE_PARAMS.add_param(MP)
BASE_PARAMS.add_param(ST)
BASE_PARAMS.add_param(ATT)
