from flask_restful import Resource
from flask import request, jsonify
from dataclasses import asdict
from viewModel.UserViewModel import UserViewModel

from serviceImpletments.userManager import userManager


class getAllUsers(Resource):
    '''取得所有使用者'''

    def get(self):
        _user = userManager()
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


class createUser(Resource):
    '''新增使用者'''

    def post(self):
        # , input: UserViewModel
        inputData = request.get_json()
        input = UserViewModel(**inputData)
        _user = userManager()
        _user.createAccount(input)
        returnJsonify = jsonify(input)
        return returnJsonify
