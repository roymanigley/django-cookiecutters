import { Component } from '@angular/core';
import { LoginService } from '../../../shared/services/auth/login.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {

  formGroup?: FormGroup;

  constructor(
    private loginService: LoginService,
    private router: Router,
    formBuilder: FormBuilder
  ){
    this.formGroup = formBuilder.group({
      username: formBuilder.control('', [Validators.required]),
      password: formBuilder.control('', [Validators.required])
    }) 
  }

  login(): void {
    if (this.formGroup?.valid) {
      this.loginService.login(this.formGroup.value).subscribe({
        next: () => this.onLoginSuccess(),
        error: () => this.onLoginFail()
      })
    }
  }

  onLoginSuccess(): void {
    this.router.navigateByUrl('/')
  }

  onLoginFail(): void {
    
  }
}
