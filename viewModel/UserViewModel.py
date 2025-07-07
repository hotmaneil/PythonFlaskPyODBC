import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class UserViewModel:
    '''輸入使用者之資料模型'''
    CODE: str
    NAME: str
    PASSWORD: str
    IS_ENABLED: bool
    IS_DELETED: bool
    CREATE_USER: Optional[str]
    CREATE_TIME: Optional[datetime.datetime]
    MODIFIER: Optional[str]
    MODIFY_TIME: Optional[datetime.datetime]