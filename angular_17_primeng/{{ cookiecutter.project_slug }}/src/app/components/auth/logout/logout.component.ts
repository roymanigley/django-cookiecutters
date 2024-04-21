import { Component, OnInit } from '@angular/core';
import { LoginService } from '../../../shared/services/auth/login.service';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrl: './logout.component.scss'
})
export class LogoutComponent implements OnInit{

  constructor(
    private loginService: LoginService
  ) {}

  ngOnInit(): void {
      this.loginService.logout().subscribe()
  }
}
