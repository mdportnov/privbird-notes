from dataclasses import dataclass
from typing import Optional

from notes.utils.Expires import Expires
from notes.utils.Network import Network
from privnote.dto.Serializable import Serializable


@dataclass
class OptionsRequest(Serializable):
    network: Network
    expires: Expires
    email: Optional[str]
