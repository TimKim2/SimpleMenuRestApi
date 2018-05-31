from myapp.models import Person
from myapp.models import Menu
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name')


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('key_name', 'store_name', 'menu_index', 'name_first', 'description_first', 'name_second',
                  'description_second')