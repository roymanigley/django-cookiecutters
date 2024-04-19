from abc import ABC, abstractmethod
from typing import Optional, Tuple

from django.core.paginator import Paginator
from django.db import models
from django.db.models import QuerySet


class AbstractRepository(ABC):

    @abstractmethod
    def get_all(
            self, *, page: int = None, size: int = None, filter_dict: dict = None
    ) -> Tuple[QuerySet[models.Model], int]:
        pass

    @abstractmethod
    def get_by_id(self, *, id) -> Optional[models.Model]:
        pass

    @abstractmethod
    def create(self, *, model_instance: object) -> models.Model:
        pass

    @abstractmethod
    def update(self, *, id, model_instance: object) -> models.Model:
        pass

    @abstractmethod
    def delete(self, *, id) -> None:
        pass


class GenericRepository(AbstractRepository):
    model_class = type[models.Model]
    query_set: QuerySet

    def __init__(self):
        assert hasattr(self, 'model_class'), f'The attribute "model_class" have to be defined for {self.__module__}.{type(self).__name__}'

    def get_all(
            self, *, page: int = None, size: int = None, filter_dict: dict = None, order_by='id'
    ) -> Tuple[QuerySet[model_class], int]:
        page = max(int(page), 1) if page else 1
        size = max(int(size), 1) if size else 25
        try:
            self.before_get_all(page=page, size=size, filter_dict=filter_dict)
            queryset = self.query_set.order_by(order_by)
            if filter_dict:
                queryset = self.query_set.filter(**filter_dict)
            paginator = Paginator(queryset.all(), size)
            total = paginator.count
            if (page - 1) * size < total:
                model_query_set = paginator.get_page(page)
            else:
                model_query_set = self.query_set.none()
            self.on_get_all_success(model_query_set=model_query_set)
            return model_query_set, total
        except Exception as e:
            return self.on_get_all_fail(page=page, size=size, filter_dict=filter_dict, exception=e)

    def get_by_id(self, *, id) -> Optional[model_class]:
        try:
            self.before_get_by_id(id=id)
            model_instance = self.model_class.objects.filter(id=id).first()
            self.on_get_by_id_success(model_instance=model_instance)
            return model_instance
        except Exception as e:
            self.on_get_by_id_fail(id=id, exception=e)

    def create(self, *, model_instance: model_class) -> model_class:
        try:
            self.before_create(model_instance=model_instance)
            model_instance.save(force_insert=True)
            self.on_create_success(model_instance=model_instance)
            return model_instance
        except Exception as e:
            return self.on_create_fail(model_instance=model_instance, exception=e)

    def update(self, *, id, model_instance: model_class) -> model_class:
        try:
            model_instance.id = id
            self.before_update(model_instance=model_instance)
            model_instance.save(force_update=True)
            self.on_update_success(model_instance=model_instance)
            return model_instance
        except Exception as e:
            return self.on_update_fail(model_instance=model_instance, exception=e)

    def delete(self, *, id) -> None:
        self.before_delete(id=id)
        try:
            self.model_class.objects.filter(id=id).delete()
            self.on_delete_success(id=id)
        except Exception as e:
            self.on_delete_fail(id=id, exception=e)

    def get_queryset(self) -> QuerySet:
        if self.query_set:
            return self.query_set
        else:
            return self.model_class.objects.all()

    def before_get_all(self, *, page: int, size: int, filter_dict: dict) -> None:
        pass

    def on_get_all_success(self, *, model_query_set: QuerySet) -> None:
        pass

    def on_get_all_fail(
            self, *, page: int, size: int, filter_dict: dict, exception: Exception
    ) -> Tuple[QuerySet[model_class], int]:
        raise exception

    def before_get_by_id(self, *, id) -> None:
        pass

    def on_get_by_id_success(self, *, model_instance: model_class) -> None:
        pass

    def on_get_by_id_fail(self, *, id, exception: Exception) -> models:
        raise exception

    def before_create(self, *, model_instance: model_class) -> None:
        pass

    def on_create_success(self, *, model_instance: model_class) -> None:
        pass

    def on_create_fail(self, *, model_instance: model_class, exception: Exception) -> model_class:
        raise exception

    def before_update(self, *, model_instance: model_class) -> None:
        pass

    def on_update_success(self, *, model_instance: model_class) -> None:
        pass

    def on_update_fail(self, *, model_instance: model_class, exception: Exception) -> model_class:
        raise exception

    def before_delete(self, *, id) -> None:
        pass

    def on_delete_success(self, *, id) -> None:
        pass

    def on_delete_fail(self, *, id, exception: Exception) -> None:
        raise exception
