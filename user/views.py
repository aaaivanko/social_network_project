from rest_framework import mixins, viewsets, permissions

from .models import CustomUser
from .permissions import ReadOnly
from .serializers import RegisterCustomUserSerializer, UserActivitySerializer


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    User Register View
    Creating User
    """
    queryset = CustomUser.objects.all()
    serializer_class = RegisterCustomUserSerializer


class UserActivityViewSet(viewsets.ModelViewSet):
    """
    User Activity View
    User last request to the server, last login
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [ReadOnly]