{% for model in cookiecutter.models.models_list %}import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AutoCompleteCompleteEvent } from 'primeng/autocomplete';
import { {{ model.name }}Service } from '../../../../shared/services/api/{{ model.name|lower }}.service';
import { {{ model.name }} } from '../../../../shared/models/domain/{{ model.name|lower }}';
{% if 'relations' in model.keys() %}{% for relation in model.relations %}import { {{ relation.type }} } from '../../../../shared/models/domain/{{ relation.type|lower }}';
import { {{ relation.type }}Service } from '../../../../shared/services/api/{{ relation.type|lower }}.service';
{% endfor %}{% endif %}

@Component({
  selector: 'app-{{ model.name|lower }}-edit',
  templateUrl: './{{ model.name|lower }}-edit.component.html',
  styleUrl: './{{ model.name|lower }}-edit.component.scss'
})
export class {{ model.name }}EditComponent {
  
  record?: {{ model.name }};
  formGroup?: FormGroup;
  {% if 'relations' in model.keys() %}{% for relation in model.relations %}filtered{{ relation.name|title }}s: {{ relation.type }}[] = [];
  {% endfor %}{% endif %}

  constructor(
    private route: ActivatedRoute,
    private service: {{ model.name }}Service,
    private formBuilder: FormBuilder,{% if 'relations' in model.keys() %}{% for relation in model.relations %}
    private {{ relation.name }}Service: {{ relation.type }}Service,{% endfor %}{% endif %}
  ) {}

  ngOnInit(): void {
    this.route.data.subscribe(data => this.record = data['record'] ?? new {{ model.name }}());

    this.formGroup = this.formBuilder.group({
      {% for field in model.fields %}
      {% if field.type in ['DateField', 'DateTimeField']%}
      {{ field.name }}: this.formBuilder.control(
        this.record?.{{ field.name }} ? new Date(this.record?.{{ field.name }}) : undefined, 
        [{% if field.required %}Validators.required{% endif %}]
      ),
      {% elif field.type == 'TimeField' %}
      {{ field.name }}: this.formBuilder.control(
        this.record?.{{ field.name }} ? new Date(`0000-01-01T${this.record?.{{ field.name }}}`) : undefined, 
        [{% if field.required %}Validators.required{% endif %}]
      ),
      {% else %}
      {{ field.name }}: this.formBuilder.control(this.record?.{{ field.name }}, [{% if field.required %}Validators.required{% endif %}]),
      {% endif %}
      {% endfor %}
      {% if 'relations' in model.keys() %}{% for relation in model.relations %}{{ relation.name }}: this.formBuilder.control(this.record?.{{ relation.name }}, [{% if relation.required %}Validators.required{% endif %}]),
      {% endfor %}{% endif %}
    });
  }

  save(): void {
    if (this.formGroup?.valid) {{'{'}}{% for field in model.fields %}{% if field.type == 'DateField' %}
      this.formGroup.value.{{ field.name }} = this.formGroup.value.{{ field.name }}?.toISOString()?.substring(0, 10);
      {% elif field.type == 'DateTimeField' %}
      this.formGroup.value.{{ field.name }} = this.formGroup.value.{{ field.name }}?.toISOString();
      {% elif field.type == 'TimeField' %}
      this.formGroup.value.{{ field.name }} = this.formGroup.value.{{ field.name }}?.toISOString()?.substring(11, 16);
      {% endif %}{% endfor %}{% if 'relations' in model.keys() %}{% for relation in model.relations %}
      this.formGroup.value.{{ relation.name }}_id = this.formGroup.value.{{ relation.name }}?.id;
      {% endfor %}{% endif %}
      if (this.record?.id) {
        this.service.update(this.record.id, this.formGroup.value).subscribe({
          next: () => this.onSaveSuccess(),
          error: () => this.onSaveError()
        });
      } else {
        this.service.create(this.formGroup.value).subscribe({
          next: () => this.onSaveSuccess(),
          error: () => this.onSaveError()
        });
      }
    }
  }

  {% if 'relations' in model.keys() %}{% for relation in model.relations %}
  filter{{ relation.name|title }}($event: AutoCompleteCompleteEvent) {
    this.{{ relation.name }}Service.getList({filter: JSON.stringify({{'{'}}{% for _model in cookiecutter.models.models_list %}{% if _model.name == relation.type %}{{_model.fields[0].name}}{% endif %}{% endfor %}__icontains: $event.query})})
      .subscribe(data => this.filtered{{ relation.name|title }}s = data.results)
  }{% endfor %}{% endif %}

  back(): void {
    history.back();
  }

  private onSaveSuccess(): void {
    this.back()
  }

  private onSaveError(): void {
    
  }
}
--- split: src/app/components/domain/{{ model.name|lower }}/{{ model.name|lower }}-edit/{{ model.name|lower }}-edit.component.ts
{% endfor %}
