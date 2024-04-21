{% for model in cookiecutter.models.models_list %}export class {{ model.name }} {
    id?: number;{%for field in model.fields%}
    {{ field.name }}?: {%- if field.type in ['IntegerField', 'FloatField', 'BigIntegerField', 'DecimalField'] -%} string
    {%- elif field.type == 'BooleanField' -%} boolean
    {%- elif field.type in ['DateField', 'DateTimeField'] -%} Date
    {%- else -%} string
    {%- endif -%};{% endfor %}
}
--- split: src/app/shared/models/domain/{{ model.name|lower }}.ts
{% endfor %}
