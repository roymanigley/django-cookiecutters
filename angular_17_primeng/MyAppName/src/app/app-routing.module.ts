import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Error404Component } from './components/errors/error404/error404.component';
import { HomeComponent } from './components/home/home.component';

const routes: Routes = [
  { path: 'cookie', loadChildren: ()=> import('./components/domain/cookie/cookie.module').then(m=> m.CookieModule) },
  { path: '', loadChildren: ()=> import('./components/auth/auth.module').then(m=> m.AuthModule) },
  { path: '404', component: Error404Component},
  { path: 'home', component: HomeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
