"""
    Public class JwtRoutes

    The main public API for flask-jwt-router with methods to
    handle JSON web tokens.

"""
from ._jwt_router import FlaskJWTRouter
from ._authentication import JWTAuthStrategy


class JwtRoutes(FlaskJWTRouter):
    """
    :param: app
    """
    def __init__(self, **kwargs):
        super(JwtRoutes, self).__init__(**kwargs)
        self.auth = JWTAuthStrategy()
