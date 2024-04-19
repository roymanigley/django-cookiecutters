from abc import abstractmethod

from django.db import models
from rest_framework import serializers


class AbstractSerializer(serializers.Serializer):

    @abstractmethod
    def to_instance(self) -> models.Model:
        pass


class GenericSerializer(AbstractSerializer):
    id = serializers.IntegerField(read_only=True)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        assert hasattr(self.Meta,
                       'model'), f'The attribute "model" have to be defined for {self.__module__}.{type(self).__name__}.Meta'

    class Meta:
        model = None
        fields = None

    def to_instance(self) -> type[Meta.model]:
        if not hasattr(self, '_validated_data'):
            self.is_valid(raise_exception=True)
        self.instance = self.Meta.model(**self.validated_data)
        return self.instance
