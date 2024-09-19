from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List

@dataclass_json
@dataclass
class Ransomware:
    name : List[str] = field(default_factory=List)
    extensions : str = ""
    extensionPattern : str = ""
    ransomNoteFilenames : str = ""
    comment : str = ""
    encryptionAlgorithm : str = ""
    decryptor : str = ""
    resources : List[str] = field(default_factory=List)
    screenshots : str = ""

@dataclass_json
@dataclass
class RansomwareSet:
    data : List[Ransomware] 

    def __post_init__(self):
        self.data=[Ransomware.from_dict(item) for item in self.data ]