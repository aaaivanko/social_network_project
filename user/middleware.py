from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from .models import CustomUser


class UserLastRequestMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            CustomUser.objects.filter(email=request.user).update(last_activity=timezone.now())
