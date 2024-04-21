from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from {{ cookiecutter.project_slug }}.views import {{ cookiecutter.models.models_list|map(attribute='name')|join('Api, ') }}Api

urlpatterns = []

router = DefaultRouter()
{% for model in cookiecutter.models.models_list %}router.register('{{ model.name|lower}}', {{ model.name }}Api, '{{ model.name|lower }}')
{% endfor %}
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDI_ROOT)

