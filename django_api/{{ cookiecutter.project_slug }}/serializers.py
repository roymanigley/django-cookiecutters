from generics.serializers import GenericSerializer
from rest_framework import serializers

from {{ cookiecutter.project_slug }}.models import {{ cookiecutter.models.models_list|map(attribute='name')|join(', ') }}

{% for model in cookiecutter.models.models_list %}
class {{model.name}}Serializer(GenericSerializer):
    {% if 'relations' in model.keys() %}
    {% for relation in model.relations %}class _{{model.name}}_{{ relation.name|replace('_', ' ')|title|replace(' ', '') }}Serializer(GenericSerializer):       
        class Meta:
            model = {{ relation.type }}
        {% for _model in cookiecutter.models.models_list %}{% if _model.name == relation.type %}{% if 'fields' in _model.keys() %}{% for _field in _model.fields %}
        {{_field.name}} = serializers.{{ _field.type }}(read_only=True)
        {% endfor %}{% endif %}{% endif %}{% endfor %}{% endfor %}{% endif %}

    id = serializers.IntegerField(read_only=True)
    {% if 'fields' in model.keys() %}{% for field in model.fields %}{{field.name}} = serializers.{{ field.type }}(
        {% if 'max_length' in field.keys() and field.max_length %}max_length={{field.max_length}}, {% endif %}
        {% if 'required' not in field.keys() or field.required in [None, True] %}required=True, {% endif %}
    )
    {% endfor %}{% endif %}
    {% if 'relations' in model.keys() %}{% for relation in model.relations %}{{relation.name}} = _{{model.name}}_{{ relation.name|replace('_', ' ')|title|replace(' ', '') }}Serializer(read_only=True)
    {{ relation.name }}_id = serializers.IntegerField(write_only=True,
        {% if 'required' not in relation.keys() or relation.required in [None, True] %}required=True, {% endif %}
    )
    {% endfor %}{% endif %}

    class Meta:
        model = {{ model.name }}

{% endfor %}
