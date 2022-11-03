from __future__ import annotations

from abc import ABC
from enum import Enum
from typing import Dict

from dacite import Config, from_dict
from rest_framework.utils import json


class Serializable(ABC):
    @classmethod
    def deserialize(cls, data: Dict) -> Serializable:
        return from_dict(cls, data, config=Config(cast=[Enum]))

    def serialize(self) -> Dict:
        return json.loads(json.dumps(self, default=lambda x: x.__dict__, sort_keys=True))
