from flask_restful import Resource
from flask import request, jsonify
from dataclasses import asdict

from serviceImpletments.userManager import userManager

class getAllUsers(Resource):
    '''取得所有使用者'''

    def get(self):
        _user=userManager()
        userList = _user.getUserList()
        returnJsonify = jsonify([asdict(user) for user in userList])
        return returnJsonify

class getOneUser(Resource):
    '''取得單一使用者資料'''

    def get(self, account):
        _user = userManager()
        userData = _user.getUserByAccount(account)
        returnJsonify = jsonify(userData)
        return returnJsonify
