{% for model in cookiecutter.models.models_list %}import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { {{ model.name }}Service } from '../../../../shared/services/api/{{ model.name|lower }}.service';
import { {{ model.name }} } from '../../../../shared/models/domain/{{ model.name|lower }}';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-{{ model.name|lower }}-edit',
  templateUrl: './{{ model.name|lower }}-edit.component.html',
  styleUrl: './{{ model.name|lower }}-edit.component.scss'
})
export class {{ model.name }}EditComponent {
  
  record?: {{ model.name }};
  formGroup?: FormGroup;

  constructor(
    private route: ActivatedRoute,
    private service: {{ model.name }}Service,
    private formBuilder: FormBuilder
  ) {}

  ngOnInit(): void {
    this.route.data.subscribe(data => this.record = data['record'] ?? new {{ model.name }}());

    this.formGroup = this.formBuilder.group({
      {% for field in model.fields %}{{ field.name }}: this.formBuilder.control(this.record?.{{ field.name }}, [Validators.required]),
      {% endfor %}
    });
  }

  save(): void {
    if (this.formGroup?.valid) {
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
