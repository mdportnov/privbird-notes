from abc import ABC
from typing import Dict

from rest_framework.utils import json


class Serializable(ABC):
    def serialize(self) -> Dict:
        return json.loads(json.dumps(self, default=lambda x: x.__dict__, sort_keys=True))
