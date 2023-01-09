from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Image
        fields = ('slug', 'title', 'image', 'author_id')
