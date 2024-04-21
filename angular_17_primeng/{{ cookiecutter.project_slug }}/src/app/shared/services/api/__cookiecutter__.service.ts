{% for model in cookiecutter.models.models_list %}import { Injectable } from '@angular/core';
import { {{ model.name }} } from '../../models/domain/{{ model.name|lower }}';
import { HttpClient } from '@angular/common/http';
import { GenericApiService } from '../../generics/generic-api-service';

@Injectable({
  providedIn: 'root'
})
export class {{ model.name }}Service extends GenericApiService<{{ model.name }}> {

  constructor(http: HttpClient) { 
    super(http, '/api/{{ model.name|lower }}/');
  }
}
--- split: src/app/shared/services/api/{{ model.name|lower }}.service.ts
{% endfor %}
