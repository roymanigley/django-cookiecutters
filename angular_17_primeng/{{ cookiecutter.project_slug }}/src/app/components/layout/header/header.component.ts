import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {

  showMenu = false;

  openMenu(): void {
    this.showMenu = true;
  }
  closeMenu(): void {
    this.showMenu = false;
  }

}
