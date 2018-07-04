from data.models import Store
from rest_framework import serializers


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ('key_number', 'name', 'description', 'menu')
