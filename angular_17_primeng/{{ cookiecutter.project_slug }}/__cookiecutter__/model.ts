{% for model in cookiecutter.models.models_list %}{% if 'relations' in model.keys() %}{% for relation in model.relations %}import { {{ relation.type }} } from "./{{ relation.type|lower }}";
{% endfor %}{% endif %}

export class {{ model.name }} {
    id?: number;{%for field in model.fields%}
    {{ field.name }}?: {%- if field.type in ['IntegerField', 'FloatField', 'BigIntegerField', 'DecimalField'] -%} string
    {%- elif field.type == 'BooleanField' -%} boolean
    {%- elif field.type in ['DateField', 'DateTimeField'] -%} Date
    {%- else -%} string
    {%- endif -%};{% endfor %}
    {% if 'relations' in model.keys() %}{% for relation in model.relations %}{{ relation.name}}?: {{ relation.type }};
    {% endfor %}{% endif %}
}
--- split: src/app/shared/models/domain/{{ model.name|lower }}.ts
{% endfor %}
