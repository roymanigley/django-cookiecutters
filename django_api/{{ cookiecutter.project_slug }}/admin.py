from django.contrib import admin

from {{ cookiecutter.project_slug }}.models import {{ cookiecutter.models.models_list|map(attribute='name')|join(', ') }}

{% for model in cookiecutter.models.models_list %}
class Member{{ model.name }}(admin.ModelAdmin):
    fields = ['{{ model.fields|join("', '",attribute="name") }}']

{% endfor %}
{% for model in cookiecutter.models.models_list %}admin.site.register({{ model.name}}, Member{{ model.name }})
{% endfor %}
