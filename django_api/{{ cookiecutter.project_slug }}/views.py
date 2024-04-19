from generics.apis import ModelApi

from {{ cookiecutter.project_slug }}.services import {{ cookiecutter.models.models_list|map(attribute='name')|join('Service, ') }}Service

{% for model in cookiecutter.models.models_list %}
class {{ model.name }}Api(ModelApi):
    service = {{ model.name }}Service()

{% endfor %}
