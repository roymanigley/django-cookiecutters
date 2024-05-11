import { NgModule } from '@angular/core';
import { CookieDeleteComponent } from './cookie-delete/cookie-delete.component';
import { CookieEditComponent } from './cookie-edit/cookie-edit.component';
import { CookieDetailComponent } from './cookie-detail/cookie-detail.component';
import { CookieListComponent } from './cookie-list/cookie-list.component';
import { RouterModule, Routes } from '@angular/router';
import { CookieDetailResolver, CookieListResolver } from '../../../shared/resolvers/cookie.resolver';
import { SharedModule } from '../../../shared/shared.module';

const routes: Routes = [
  { path: '', component: CookieListComponent, resolve: {records: CookieListResolver}, runGuardsAndResolvers: 'always'},
  { path: 'new', component: CookieEditComponent},
  { path: ':id/edit', component: CookieEditComponent, resolve: { record: CookieDetailResolver }},
  { path: ':id/delete', component: CookieDeleteComponent, resolve: { record: CookieDetailResolver }},
  { path: ':id', component: CookieDetailComponent, resolve: { record: CookieDetailResolver }},
];

@NgModule({
  declarations: [
    CookieDeleteComponent,
    CookieEditComponent,
    CookieDetailComponent,
    CookieListComponent
  ],
  imports: [
    RouterModule.forChild(routes),
    SharedModule
  ],
  exports: [RouterModule]
})
export class CookieModule { }
