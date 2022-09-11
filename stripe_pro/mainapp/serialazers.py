from rest_framework.serializers import ModelSerializer
from .models import Item


class ItemModelSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'