from generics.repositories import GenericRepository

from {{ cookiecutter.project_slug }}.models import {{ cookiecutter.models.models_list|map(attribute='name')|join(', ') }}

{% for model in cookiecutter.models.models_list %}
class {{ model.name }}Repository(GenericRepository):
    model_class = {{ model.name }}
    query_set = {{ model.name }}.objects.all()

{% endfor %}
