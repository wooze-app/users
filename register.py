import os
import json
from flask import views, request, jsonify, session, Response

from users import RegisterUser, Credentials, Assets

import clint


class RegisterUserView(views.MethodView):
    required_fields = ["username", "email", "password"]

    def post(self):
        token = os.getenv("TOKEN")

        data = dict(request.values)
        valid = self.search_required_fields(self.required_fields, data)
        if not valid:
            return jsonify(status=404, message="No required fields")

        request_token_value = (data.get("token") or data.get("TOKEN")).strip()
        print(clint.textui.colored.red(request_token_value))
        print(clint.textui.colored.green(token))

        if request_token_value != token:
            return Response(json.dumps({"message": "Invalid token"}), status=401)

        username, email, password = self.find_credentials(data)
        register = RegisterUser(
            username, Credentials(email, password), Assets(str(None), str(None))
        ).register_new_user(username)
        print(session)

        if isinstance(register, str):
            return jsonify(status=200, message=register)

        return jsonify(status=200, message="Success")

    def search_required_fields(self, required, data):
        for required_field in required:
            if not required_field in data:
                return False

        return True

    def find_credentials(self, data):
        return (data.get("username"), data.get("email"), data.get("password"))
