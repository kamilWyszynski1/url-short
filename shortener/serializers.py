from rest_framework import serializers

from shortener.models import Shortcut


class ShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortcut
        fields = ('url', 'short', 'pk')


class ShortcutSerializerShort(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shortcut
        fields = ('short',)
