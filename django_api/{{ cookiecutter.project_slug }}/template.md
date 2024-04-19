# {{ cookiecutter.project_slug }}

## Models
from django.db import models

{% for model in cookiecutter.models.models_list %}
class {{model.name}}(models.Model)
    {% for field in model.fields %}{{field.name}}
    {% endfor %}
{% endfor %}

## Repositories
from generics.repositories import GenericRepository

from {{ cookiecutter.project_slug }}.models import {{ cookiecutter.models.models_list|map(attribute='name')|join(', ') }}

{% for model in cookiecutter.models.models_list %}
class {{ model.name }}Repository(GenericRepository):
    model_class = {{ model.name }}
    query_set = {{ model.name }}.all()

{% endfor %}

## Services
from generics.services import GenericService

from {{ cookiecutter.project_slug }}.repositories import {{ cookiecutter.models.models_list|map(attribute='name')|join('Repository, ') }}Repository
from {{ cookiecutter.project_slug }}.serializers import {{ cookiecutter.models.models_list|map(attribute='name')|join('Serializer, ') }}Serializer
from {{ cookiecutter.project_slug }}.models import {{ cookiecutter.models.models_list|map(attribute='name')|join(', ') }}

{% for model in cookiecutter.models.models_list %}
class {{ model.name }}Service(GenericService):
    repository = {{ model.name }}Repository()
    serializer_class = {{ model.name }}Serializer

{% endfor %}

## Serializers
from generics.serializers import GenericSerializer

from {{ cookiecutter.project_slug }}.models import {{ cookiecutter.models.models_list|map(attribute='name')|join(', ') }}

{% for model in cookiecutter.models.models_list %}
class {{model.name}}Serializer(GenericSerializer):
    
    class Meta:
        model = {{ model.name }}
        fields = '__all__'

{% endfor %}

## APIs
from generics.apis import GenericApi

from {{ cookiecutter.project_slug }}.servies import {{ cookiecutter.models.models_list|map(attribute='name')|join('Service, ') }}Service

{% for model in cookiecutter.models.models_list %}
class {{ model.name }}Service(GenericApi):
    service = {{ model.name }}Service()

{% endfor %}

## URLs
from rest_framework.routers import DefaultRouter

from {{ cookiecutter.project_slug }}.views import {{ cookiecutter.models.models_list|map(attribute='name')|join('Api, ') }}Api


router = DefaultRouter()
{% for model in cookiecutter.models.models_list %}router.register('{{ model.name|lower}}', {{ model.name }}Api, '{{ model.name|lower }}')
{% endfor %}
urlpatterns += router.urls

