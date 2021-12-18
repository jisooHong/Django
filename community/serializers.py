from rest_framework import serializers
from .models import Article

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('name','title','contents','url','email','cdate') # 필드설정