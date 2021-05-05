from django.db.models import Count
from rest_framework import viewsets, status, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer, LikesAmountAnalyticSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    Post View Set
    Return Posts with additional extra actions
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    @action(detail=True,
            methods=['post'],
            permission_classes=[permissions.IsAuthenticated],
            url_path='like',
            url_name='like')
    def like(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        like = post.post_like(user_id=request.user.id)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True,
            methods=['patch'],
            permission_classes=[permissions.IsAuthenticated],
            url_path='unlike',
            url_name='unlike')
    def unlike(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.post_unlike(user_id=request.user.id)
        return Response(status=status.HTTP_200_OK)


class LikesAmountAnalyticListView(generics.ListAPIView):
    """
    Like Amount Analytic View
    Returns analytic about likes to specific date
    """
    serializer_class = LikesAmountAnalyticSerializer

    def get_queryset(self):
        queryset = Like.objects.all()
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        if date_from is not None and date_to is not None:
            queryset = (
                queryset.filter(date_created__gte=date_from, date_created__lte=date_to)
                    .extra(select={'day': "date(date_created)"})
                    .values('day')
                    .order_by('day')
                    .annotate(count=Count('date_created'))
            )
            return queryset


