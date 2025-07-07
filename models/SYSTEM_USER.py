import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class SYSTEM_USER:
    '''系統使用者'''
    ID: int
    CODE: str
    NAME: str
    PASSWORD: str
    IS_ENABLED: bool
    IS_DELETED: bool
    CREATE_USER: Optional[str]
    CREATE_TIME: Optional[datetime.datetime]
    MODIFIER: Optional[str]
    MODIFY_TIME: Optional[datetime.datetime]
