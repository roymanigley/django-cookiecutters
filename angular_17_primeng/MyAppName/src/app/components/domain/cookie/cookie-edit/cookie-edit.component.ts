import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CookieService } from '../../../../shared/services/api/cookie.service';
import { Cookie } from '../../../../shared/models/domain/cookie';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-cookie-edit',
  templateUrl: './cookie-edit.component.html',
  styleUrl: './cookie-edit.component.scss'
})
export class CookieEditComponent {
  
  record?: Cookie;
  formGroup?: FormGroup;

  constructor(
    private route: ActivatedRoute,
    private service: CookieService,
    private formBuilder: FormBuilder
  ) {}

  ngOnInit(): void {
    this.route.data.subscribe(data => this.record = data['record'] ?? new Cookie());

    this.formGroup = this.formBuilder.group({
      name: this.formBuilder.control(this.record?.name, [Validators.required])
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
