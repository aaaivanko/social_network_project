from rest_framework import routers

from django.urls import path, include

from .views import PostViewSet, LikesAmountAnalyticListView


router = routers.DefaultRouter()

# Post creation

router.register(r'posts', PostViewSet, basename='posts')


urlpatterns = [
    path('', include(router.urls)),
    path('analytics/', LikesAmountAnalyticListView.as_view())
]
