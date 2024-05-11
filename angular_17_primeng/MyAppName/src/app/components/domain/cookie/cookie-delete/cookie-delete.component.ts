import { Component } from '@angular/core';
import { CookieService } from '../../../../shared/services/api/cookie.service';
import { ActivatedRoute } from '@angular/router';
import { Cookie } from '../../../../shared/models/domain/cookie';

@Component({
  selector: 'app-cookie-delete',
  templateUrl: './cookie-delete.component.html',
  styleUrl: './cookie-delete.component.scss'
})
export class CookieDeleteComponent {

  record?: Cookie;

  constructor(
    private route: ActivatedRoute,
    private service: CookieService
  ) {}

  ngOnInit(): void {
    this.route.data.subscribe(data => this.record = data['record'] ?? new Cookie());
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
