from typing import List, Optional, Tuple
from rpg.bf_rpg.entities import Character, Skill, Param, Trait, Item
from rpg.bf_rpg.repositories import ITraitRepository, ISkillRepository, IItemRepository, IParamRepository, ICharacterRepository, IEntityRepository

StaticRepositories = Tuple[ICharacterRepository, IParamRepository, IItemRepository, ISkillRepository, ITraitRepository]


class CharacterLogic:
    def __init__(self,
                 characters: ICharacterRepository,
                 skills: ISkillRepository,
                 traits: ITraitRepository,
                 items: IItemRepository,
                 params: IParamRepository):
    pass


class ItemLogic:
    pass

class ParamLogic:
    pass

class TraitLogic:
    pass

class SkillLogic:
    pass
