
from models.SYSTEM_USER import SYSTEM_USER
from serviceImpletments.db import get_connection
from serviceImpletments.query_utils import query, insertRecord
from dataclasses import asdict
from viewModel.UserViewModel import UserViewModel

conn = get_connection()


class userManager:
    '''實做使用者'''

    def getUserList(self):
        '''使用pyodbc取得使用者列表'''
        try:
            result = query(
                conn, "SELECT * FROM [SYSTEM_USER]", model=SYSTEM_USER)
            return result

        except RuntimeError as e:
            print("RuntimeError錯誤", e)
        finally:
            print("getUserListByDapper data", result)

    def getUserByAccount(self, account):
        '''使用pyodbc取得單一使用者資料'''
        try:
            result = query(
                conn,
                "SELECT * FROM [SYSTEM_USER] WHERE [CODE] = ?",
                model=SYSTEM_USER,
                params=(account,)
            )
            return result
        except SystemError as e:
            print("SystemError 錯誤", e)

    def createAccount(self, input: UserViewModel):
        '''使用pyodbc新增使用者資料'''
        try:
            userDict = asdict(input)
            result = insertRecord(conn, 'SYSTEM_USER', userDict)
            return result
        except SystemError as e:
            print("SystemError 錯誤", e)
