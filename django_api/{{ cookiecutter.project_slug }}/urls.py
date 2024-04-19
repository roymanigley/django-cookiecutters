from rest_framework.routers import DefaultRouter

from {{ cookiecutter.project_slug }}.views import {{ cookiecutter.models.models_list|map(attribute='name')|join('Api, ') }}Api

urlpatterns = []

router = DefaultRouter()
{% for model in cookiecutter.models.models_list %}router.register('{{ model.name|lower}}', {{ model.name }}Api, '{{ model.name|lower }}')
{% endfor %}
urlpatterns += router.urls
