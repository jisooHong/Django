from rest_framework import viewsets
from .serializers import CommunitySerializer
from .models import Article

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    print(queryset)
    serializer_class = CommunitySerializer
