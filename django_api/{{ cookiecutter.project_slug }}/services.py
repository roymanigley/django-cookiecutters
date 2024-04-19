from generics.services import GenericService

from {{ cookiecutter.project_slug }}.repositories import {{ cookiecutter.models.models_list|map(attribute='name')|join('Repository, ') }}Repository
from {{ cookiecutter.project_slug }}.serializers import {{ cookiecutter.models.models_list|map(attribute='name')|join('Serializer, ') }}Serializer
from {{ cookiecutter.project_slug }}.models import {{ cookiecutter.models.models_list|map(attribute='name')|join(', ') }}

{% for model in cookiecutter.models.models_list %}
class {{ model.name }}Service(GenericService):
    repository = {{ model.name }}Repository()
    serializer_class = {{ model.name }}Serializer

{% endfor %}
