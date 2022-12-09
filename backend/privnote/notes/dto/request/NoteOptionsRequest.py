from dataclasses import dataclass
from typing import Optional

from notes.utils.Expires import Expires
from notes.utils.Network import Network
from privnote.dto.Serializable import Serializable


@dataclass
class NoteOptionsRequest(Serializable):
    email: Optional[str]
    expires: Expires = Expires.YEAR
    network: Network = Network.HTTPS
