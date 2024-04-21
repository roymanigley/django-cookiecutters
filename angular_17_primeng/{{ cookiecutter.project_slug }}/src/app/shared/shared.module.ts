import { HttpClient, HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UiFrameworkModule } from './ui-framework/ui-framework.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MissingTranslationHandler, TranslateLoader, TranslateModule, TranslatePipe } from '@ngx-translate/core';
import { CustomMissingTranslationHandler, HttpLoaderFactory } from './utils/translation-utils';


@NgModule({
  declarations: [
  ],
  imports: [
    CommonModule,
    UiFrameworkModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    TranslateModule.forRoot(
      {
        defaultLanguage: 'en',
        missingTranslationHandler: {provide: MissingTranslationHandler, useClass: CustomMissingTranslationHandler},
        loader: {
            provide: TranslateLoader,
            useFactory: HttpLoaderFactory,
            deps: [HttpClient]
        }
      }
    ),
  ],
  exports: [
    CommonModule,
    UiFrameworkModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    TranslateModule,
  ]
})
export class SharedModule { }
