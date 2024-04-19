import enum
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from django.db import models
from django.db.models import QuerySet

from generics.repositories import AbstractRepository
from generics.serializers import AbstractSerializer


class AbstractService(ABC):
    serializer_class: type[AbstractSerializer]
    serializer_class_get_all: type[AbstractSerializer] = None
    serializer_class_get_by_id: type[AbstractSerializer] = None
    serializer_class_create: type[AbstractSerializer] = None
    serializer_class_update: type[AbstractSerializer] = None
    serializer_class_update_partial: type[AbstractSerializer] = None
    serializer_class_delete: type[AbstractSerializer] = None

    @abstractmethod
    def get_all(self, *, page: int = None, size: int = None, filter_dict: dict = None) -> Tuple[List[dict], int]:
        pass

    @abstractmethod
    def get_by_id(self, *, id) -> Optional[dict]:
        pass

    @abstractmethod
    def create(self, *, data: dict) -> dict:
        pass

    @abstractmethod
    def update(self, *, id, data: dict) -> dict:
        pass

    @abstractmethod
    def update_partial(self, *, id, data: dict) -> dict:
        pass

    @abstractmethod
    def delete(self, *, id) -> None:
        pass

    @classmethod
    def get_serializer_class(cls, operation: 'ServiceOperation' = None) -> type[AbstractSerializer]:
        if operation == ServiceOperation.GET_ALL and cls.serializer_class_get_all:
            return cls.serializer_class_get_all
        elif operation == ServiceOperation.GET_BY_ID and cls.serializer_class_get_by_id:
            return cls.serializer_class_get_by_id
        elif operation == ServiceOperation.CREATE and cls.serializer_class_create:
            return cls.serializer_class_create
        elif operation == ServiceOperation.UPDATE and cls.serializer_class_update:
            return cls.serializer_class_update
        elif operation == ServiceOperation.UPDATE_PARTIAL and cls.serializer_class_update_partial:
            return cls.serializer_class_update_partial
        elif operation == ServiceOperation.DELETE and cls.serializer_class_delete:
            return cls.serializer_class_delete
        else:
            return cls.serializer_class


class ServiceOperation(enum.Enum):
    GET_ALL = 'GET_ALL'
    GET_BY_ID = 'GET_BY_ID'
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    UPDATE_PARTIAL = 'UPDATE_PARTIAL'
    DELETE = 'DELETE'


class GenericService(AbstractService):
    repository: AbstractRepository
    serializer_class: type[AbstractSerializer]

    def __init__(self):
        assert hasattr(self,
                       'repository'), f'The attribute "repository" have to be defined for {self.__module__}.{type(self).__name__}'
        assert hasattr(self,
                       'serializer_class'), f'The attribute "serializer_class" have to be defined for {self.__module__}.{type(self).__name__}'

    def get_all(self, *, page: int = None, size: int = None, filter_dict: dict = None) -> Tuple[List[dict], int]:
        serializer_class = self.get_serializer_class(ServiceOperation.GET_ALL)
        try:
            self.before_get_all(page=page, size=size, filter_dict=filter_dict)
            model_query_set, total_record_count = self.repository.get_all(page=page, size=size, filter_dict=filter_dict)
            self.on_get_all_success(model_query_set=model_query_set)
            serializer = serializer_class(model_query_set, many=True)
            return serializer.data, total_record_count
        except Exception as e:
            return self.on_get_all_fail(page=page, size=size, filter_dict=filter_dict, exception=e)

    def get_by_id(self, *, id) -> Optional[dict]:
        serializer_class = self.get_serializer_class(ServiceOperation.GET_BY_ID)
        try:
            self.before_get_by_id(id=id)
            model_instance = self.repository.get_by_id(id=id)
            self.on_get_by_id_success(model_instance=model_instance)
            if model_instance:
                serializer = serializer_class(model_instance)
                return serializer.data
            return None
        except Exception as e:
            return self.on_get_by_id_fail(id=id, exception=e)

    def create(self, *, data: dict) -> dict:
        serializer_class = self.get_serializer_class(ServiceOperation.CREATE)
        try:
            serializer = serializer_class(data=data)
            model_instance = serializer.to_instance()
            self.before_create(model_instance=model_instance)
            model_instance = self.repository.create(model_instance=model_instance)
            self.on_create_success(model_instance=model_instance)
            serializer.instance = model_instance
            return serializer.data
        except Exception as e:
            return self.on_create_fail(data=data, exception=e)

    def update(self, *, id, data: dict) -> dict:
        serializer_class = self.get_serializer_class(ServiceOperation.UPDATE)
        try:
            serializer = serializer_class(data=data, partial=False)
            model_instance = serializer.to_instance()
            self.before_update(model_instance=model_instance)
            model_instance = self.repository.update(id=id, model_instance=model_instance)
            self.on_update_success(model_instance=model_instance)
            serializer.instance = model_instance
            return serializer.data
        except Exception as e:
            return self.on_update_fail(data=data, exception=e)

    def update_partial(self, *, id, data: dict) -> dict:
        serializer_class = self.get_serializer_class(ServiceOperation.UPDATE_PARTIAL)
        try:
            serializer = serializer_class(data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            model_instance = self.repository.get_by_id(id=id)
            for key, value in serializer.validated_data.items():
                model_instance.__setattr__(key, value)
            self.before_update(model_instance=model_instance)
            model_instance = self.repository.update(id=id, model_instance=model_instance)
            self.on_update_success(model_instance=model_instance)
            serializer.instance = model_instance
            return serializer.data
        except Exception as e:
            return self.on_update_fail(data=data, exception=e)

    def delete(self, *, id) -> None:
        try:
            self.before_delete(id=id)
            self.repository.delete(id=id)
        except Exception as e:
            self.on_delete_fail(id=id, exception=e)
        self.on_delete_success(id=id)

    def before_get_all(self, *, page: int = None, size: int = None, filter_dict: dict = None) -> None:
        pass

    def on_get_all_success(self, *, model_query_set: QuerySet[models.Model]) -> None:
        pass

    def on_get_all_fail(
            self, *, page: int = None, size: int = None, filter_dict: dict = None, exception: Exception
    ) -> Tuple[List[dict], int]:
        raise exception

    def before_get_by_id(self, *, id) -> None:
        pass

    def on_get_by_id_success(self, *, model_instance: models.Model) -> None:
        pass

    def on_get_by_id_fail(self, *, id, exception: Exception) -> Optional[dict]:
        raise exception

    def before_create(self, *, model_instance: models.Model) -> None:
        pass

    def on_create_success(self, *, model_instance: models.Model) -> None:
        pass

    def on_create_fail(self, *, data: dict, exception: Exception) -> dict:
        raise exception

    def before_update(self, *, model_instance: models.Model) -> None:
        pass

    def on_update_success(self, *, model_instance: models.Model) -> None:
        pass

    def on_update_fail(self, *, data: dict, exception: Exception) -> dict:
        raise exception

    def before_delete(self, *, id) -> None:
        pass

    def on_delete_success(self, *, id) -> None:
        pass

    def on_delete_fail(self, *, id, exception: Exception) -> None:
        raise exception
