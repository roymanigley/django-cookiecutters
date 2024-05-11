{% for model in cookiecutter.models.models_list %}import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { {{ model.name }} } from '../../../../shared/models/domain/{{ model.name|lower }}';
import { IPage } from '../../../../shared/generics/generic-api-service';
import { PaginatorState } from 'primeng/paginator';
import { every } from 'rxjs';
import { DEFAULT_PAGE_SIZE } from '../../../../shared/constants';

@Component({
  selector: 'app-{{ model.name|lower }}-list',
  templateUrl: './{{ model.name|lower }}-list.component.html',
  styleUrl: './{{ model.name|lower }}-list.component.scss'
})
export class {{ model.name }}ListComponent implements OnInit {

  page?: IPage<{{ model.name }}>;
  defaultPageSize = DEFAULT_PAGE_SIZE

  constructor(
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.route.data.subscribe(data => this.page = data['records'])
  }
  
  onPageChange($event: PaginatorState) {
    const baseUrl = this.router.url.split('?')[0]
    this.router.navigateByUrl(`${baseUrl}?page=${($event.page ?? 0) +1}&size=${$event.rows}`)
  }
}
--- split: src/app/components/domain/{{ model.name|lower }}/{{ model.name|lower }}-list/{{ model.name|lower }}-list.component.ts
{% endfor %}
