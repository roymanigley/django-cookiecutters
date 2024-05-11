{% for model in cookiecutter.models.models_list %}import { NgModule } from '@angular/core';
import { {{ model.name }}DeleteComponent } from './{{ model.name|lower }}-delete/{{ model.name|lower }}-delete.component';
import { {{ model.name }}EditComponent } from './{{ model.name|lower }}-edit/{{ model.name|lower }}-edit.component';
import { {{ model.name }}DetailComponent } from './{{ model.name|lower }}-detail/{{ model.name|lower }}-detail.component';
import { {{ model.name }}ListComponent } from './{{ model.name|lower }}-list/{{ model.name|lower }}-list.component';
import { RouterModule, Routes } from '@angular/router';
import { {{ model.name }}DetailResolver, {{ model.name }}ListResolver } from '../../../shared/resolvers/{{ model.name|lower }}.resolver';
import { SharedModule } from '../../../shared/shared.module';

const routes: Routes = [
  { path: '', component: {{ model.name }}ListComponent, resolve: {records: {{ model.name }}ListResolver}, runGuardsAndResolvers: 'always'},
  { path: 'new', component: {{ model.name }}EditComponent},
  { path: ':id/edit', component: {{ model.name }}EditComponent, resolve: { record: {{ model.name }}DetailResolver }},
  { path: ':id/delete', component: {{ model.name }}DeleteComponent, resolve: { record: {{ model.name }}DetailResolver }},
  { path: ':id', component: {{ model.name }}DetailComponent, resolve: { record: {{ model.name }}DetailResolver }},
];

@NgModule({
  declarations: [
    {{ model.name }}DeleteComponent,
    {{ model.name }}EditComponent,
    {{ model.name }}DetailComponent,
    {{ model.name }}ListComponent
  ],
  imports: [
    RouterModule.forChild(routes),
    SharedModule
  ],
  exports: [RouterModule]
})
export class {{ model.name }}Module { }
--- split: src/app/components/domain/{{ model.name|lower }}/{{ model.name|lower }}.module.ts
{% endfor %}
