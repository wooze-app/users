import datetime
import jwt


class EncodeAuthToken(object):
    def __init__(self, app, username, email):
        self.encode_data = f"{username}/{email}"
        self.app = app

    def encode(self):
        try:
            current_time = datetime.datetime.utcnow()
            jwt_token_payload = {
                "exp": current_time + datetime.timedelta(days=0, seconds=60),
                "iat": current_time,
                "sub": self.encode_data,
            }
            return jwt.encode(
                jwt_token_payload, self.aoo.config.get("SECRET_KEY"), algorithm="HS256"
            )
        except Exception as exception:
            return exception

    @staticmethod
    def decode_auth_token(auth_token, app):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get("SECRET_KEY"))
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
