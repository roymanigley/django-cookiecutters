from django.db import models

{% for model in cookiecutter.models.models_list %}
class {{model.name}}(models.Model):
    {% if 'fields' in model.keys() %}{% for field in model.fields %}{{field.name}} = models.{{ field.type }}(
        {% if 'max_length' in field.keys() and field.max_length %}max_length={{field.max_length}}, {% endif %}
        {% if 'required' in field.keys() and field.required == False %}null=True, {% endif %}
    )
    {% endfor %}{% endif %}
    {% if 'relations' in model.keys() %}{% for relation in model.relations %}{{relation.name}} = models.ForeignKey('{{ relation.type }}',
        {% if 'required' in relation.keys() and relation.required == False %}null=True, {% endif %}
        on_delete=models.DO_NOTHING
    )
    {% endfor %}{% endif %}
    def __str__(self):
        return f'[{self.id}] {% if 'fields' in model.keys() and model.fields|length > 0 %}{self.{{model.fields[0].name}}}{% endif %}'
{% endfor %}
