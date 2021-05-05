from rest_framework import routers
from django.urls import path, include

from .views import UserRegisterViewSet, UserActivityViewSet

router = routers.SimpleRouter()

# urls for User registration and User activity

router.register('signup', UserRegisterViewSet, basename='register')
router.register('activity', UserActivityViewSet, basename='activity')


urlpatterns = [
    path('', include(router.urls))
]