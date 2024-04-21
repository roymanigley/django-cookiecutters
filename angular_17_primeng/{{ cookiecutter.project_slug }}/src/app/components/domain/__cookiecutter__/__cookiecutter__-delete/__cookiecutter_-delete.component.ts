{% for model in cookiecutter.models.models_list %}import { Component } from '@angular/core';
import { {{ model.name }}Service } from '../../../../shared/services/api/{{ model.name|lower }}.service';
import { ActivatedRoute } from '@angular/router';
import { {{ model.name }} } from '../../../../shared/models/domain/{{ model.name|lower }}';

@Component({
  selector: 'app-{{ model.name|lower }}-delete',
  templateUrl: './{{ model.name|lower }}-delete.component.html',
  styleUrl: './{{ model.name|lower }}-delete.component.scss'
})
export class {{ model.name }}DeleteComponent {

  record?: {{ model.name }};

  constructor(
    private route: ActivatedRoute,
    private service: {{ model.name }}Service
  ) {}

  ngOnInit(): void {
    this.route.data.subscribe(data => this.record = data['record'] ?? new {{ model.name }}());
  }

  delete(): void {
    this.service.delete(this.record!.id!).subscribe({
      next: () => this.onDeleteSuccess(),
      error: () => this.onDeleteError()
    })
  }

  back(): void {
    history.back();
  }

  private onDeleteSuccess(): void {
    this.back()
  }

  private onDeleteError(): void {
    
  }
}
--- split: src/app/components/domain/{{ model.name|lower }}/{{ model.name|lower }}-delete/{{ model.name|lower }}-delete.component.ts
{% endfor %}
