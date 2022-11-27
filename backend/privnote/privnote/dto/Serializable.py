from __future__ import annotations

import dataclasses
from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple

from dacite import Config, from_dict
from drf_yasg.openapi import Schema, TYPE_OBJECT


@dataclass(kw_only=True)
class Serializable(ABC):
    exclude: Tuple[str] = ('exclude',)

    @classmethod
    def deserialize(cls, data: Dict) -> Serializable:
        return from_dict(cls, data, config=Config(cast=[Enum]))

    def serialize(self) -> Dict:
        return dataclasses.asdict(
            self, dict_factory=lambda x: {k: v for (k, v) in x if k not in self.exclude}
        )

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT
        )
