import { Component, OnInit } from '@angular/core';
import { LanguageService } from './shared/services/language.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {

  constructor(
    private languageService: LanguageService
  ){}

  ngOnInit(): void {
      this.languageService.init();
  }
}
