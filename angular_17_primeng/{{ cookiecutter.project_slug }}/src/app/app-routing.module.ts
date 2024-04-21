import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Error404Component } from './components/errors/error404/error404.component';
import { HomeComponent } from './components/home/home.component';

const routes: Routes = [{% for model in cookiecutter.models.models_list %}
  { path: '{{ model.name|lower }}', loadChildren: ()=> import('./components/domain/{{ model.name|lower }}/{{ model.name|lower }}.module').then(m=> m.{{ model.name }}Module) },{% endfor %}
  { path: '', loadChildren: ()=> import('./components/auth/auth.module').then(m=> m.AuthModule) },
  { path: '404', component: Error404Component},
  { path: 'home', component: HomeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
