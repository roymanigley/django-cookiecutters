import json
from builtins import type

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from generics.serializers import AbstractSerializer
from generics.services import AbstractService


class ApiListMixIn:

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='filter', type=OpenApiTypes.STR,
                examples=[
                    OpenApiExample(
                        name='filter by name case insensitive',
                        value='{"name__icontains": "foo"}'
                    ),
                    OpenApiExample(
                        name='filter where id in',
                        value='{"id__in": [1,2,3,4]}'
                    ),
                    OpenApiExample(
                        name='filter by range',
                        value='{"date__range": ["2024-03-14", "2024-05-04"]}'
                    ),
                    OpenApiExample(
                        name='filter for not null',
                        value='{"name__isnull": false}'
                    ),
                ]
            ),
            OpenApiParameter(
                name='page', type=OpenApiTypes.INT
            ),
            OpenApiParameter(
                name='size', type=OpenApiTypes.INT
            ),
        ]
    )
    def list(self, request: Request) -> Response:
        page = request.query_params.get('page', None)
        size = request.query_params.get('size', None)
        filter_params = request.query_params.get('filter', None)
        filter_dict = None
        if filter_params:
            filter_dict = json.loads(filter_params)
        data, total_records_count = self.service.get_all(page=page, size=size, filter_dict=filter_dict)
        return Response(
            data,
            status=status.HTTP_200_OK,
            headers={'total-records-count': total_records_count}
        )


class ApiCreateMixIn:
    def create(self, request: Request) -> Response:
        return Response(
            self.service.create(data=request.data),
            status=status.HTTP_200_OK
        )


class ApiUpdateMixIn:

    def update(self, request: Request, id) -> Response:
        return Response(
            self.service.update(id=id, data=request.data),
            status=status.HTTP_200_OK
        )


class ApiPartialUpdateMixIn:
    def partial_update(self, request: Request, id) -> Response:
        return Response(
            self.service.update_partial(id=id, data=request.data),
            status=status.HTTP_200_OK
        )


class ApiRetrieveMixIn:
    def retrieve(self, request: Request, id) -> Response:
        data = self.service.get_by_id(id=id)
        return Response(
            data,
            status=(status.HTTP_200_OK if data else status.HTTP_404_NOT_FOUND)
        )


class ApiDeleteMixIn:
    def delete(self, request: Request, id) -> Response:
        self.service.delete(id=id)
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class GenericApi(
    ViewSet
):
    service: AbstractService
    serializer_class: type[AbstractSerializer]
    lookup_field = 'id'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert hasattr(self, 'service'), f'The attribute "service" have to be defined for {self.__module__}.{type(self).__name__}'
        self.serializer_class = self.service.serializer_class


class ModelApi(
    ApiListMixIn,
    ApiCreateMixIn,
    ApiUpdateMixIn,
    ApiPartialUpdateMixIn,
    ApiRetrieveMixIn,
    ApiDeleteMixIn,
    GenericApi
):
    pass
