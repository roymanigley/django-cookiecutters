import { Injectable } from '@angular/core';
import {TranslateService} from '@ngx-translate/core';
import { LocalStorageKey, LocalStorageService } from './local-storage.service';

@Injectable({
  providedIn: 'root'
})
export class LanguageService {

  readonly availableLanguages = ['de', 'en', 'fr'];
  readonly defaultLanguage = 'en';

  constructor(
    private localStorageService: LocalStorageService,
    private translationService: TranslateService
  ) { }

  init(): void {
    let selectedLanguage = this.localStorageService.get(LocalStorageKey.LANGUAGE);
    if (!selectedLanguage) {
      selectedLanguage = this.translationService.getBrowserLang();
    }
    this.useLanguage(selectedLanguage)
  }

  useLanguage(language: string) {
    const validLanguage = this.availableLanguages.find(l => l === language) ?? this.defaultLanguage;
    this.localStorageService.set(LocalStorageKey.LANGUAGE, validLanguage);
    this.translationService.use(validLanguage);
  }
}
