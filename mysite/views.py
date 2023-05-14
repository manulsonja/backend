from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt import serializers

class TokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = serializers.TokenObtainPairSerializer