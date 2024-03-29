from dataclasses import dataclass, field
from typing import List, Dict

PARAM_STARTING_VALUE = 100


def default_field(obj):
    return field(default_factory=lambda: obj)


class BaseEntity:
    pass


@dataclass(frozen=True)
class Param(BaseEntity):
    id: int
    name: str
    max_value: int = 0
    current_value: int = 0


@dataclass(frozen=True)
class Skill(BaseEntity):
    id: int
    name: str
    description: str
    self_effect: Dict[Param, int] = field(default_factory=dict)
    enemy_effect: Dict[Param, int] = field(default_factory=dict)


@dataclass(frozen=True)
class Trait(BaseEntity):
    id: int
    name: str
    affected_params: Dict[Param, int] = field(default_factory=dict)
    gained_skills: List[Skill] = field(default_factory=list)


@dataclass(frozen=True)
class Item(BaseEntity):
    id: int
    name: str
    value: int = 0
    weight: int = 0
    traits: List[Trait] = field(default_factory=list)


@dataclass
class Character(BaseEntity):
    id: int
    name: str
    items: List[Item] = field(default_factory=list)
    traits: List[Trait] = field(default_factory=list)
    skills: List[Skill] = field(default_factory=list)
    params: List[Param] = field(default_factory=list)
