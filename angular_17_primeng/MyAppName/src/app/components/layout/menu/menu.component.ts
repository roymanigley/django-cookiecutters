import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { LoginService } from '../../../shared/services/auth/login.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.scss'
})
export class MenuComponent implements OnInit {

  @Output() onClose = new EventEmitter<void>();
  currentUser: any = null

  constructor(
    private loginService: LoginService
  ) {
  }

  ngOnInit(): void {
    this.loginService.getCurrentUser()
        .subscribe(user => this.currentUser = user);
  }
  
  closeCallback() {
    this.onClose.emit();
  }
}
