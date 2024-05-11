import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Cookie } from '../../../../shared/models/domain/cookie';
import { IPage } from '../../../../shared/generics/generic-api-service';
import { PaginatorState } from 'primeng/paginator';
import { every } from 'rxjs';
import { DEFAULT_PAGE_SIZE } from '../../../../shared/constants';

@Component({
  selector: 'app-cookie-list',
  templateUrl: './cookie-list.component.html',
  styleUrl: './cookie-list.component.scss'
})
export class CookieListComponent implements OnInit {

  page?: IPage<Cookie>;
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
