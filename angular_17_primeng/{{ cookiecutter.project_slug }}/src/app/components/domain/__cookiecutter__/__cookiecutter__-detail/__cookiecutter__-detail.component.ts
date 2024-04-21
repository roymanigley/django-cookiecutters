{% for model in cookiecutter.models.models_list %}import { Component } from '@angular/core';

@Component({
  selector: 'app-{{ model.name|lower }}-detail',
  templateUrl: './{{ model.name|lower }}-detail.component.html',
  styleUrl: './{{ model.name|lower }}-detail.component.scss'
})
export class {{ model.name }}DetailComponent {

}
--- split: src/app/components/domain/{{ model.name|lower }}/{{ model.name|lower }}-detail/{{ model.name|lower }}-detail.component.ts
{% endfor %}
