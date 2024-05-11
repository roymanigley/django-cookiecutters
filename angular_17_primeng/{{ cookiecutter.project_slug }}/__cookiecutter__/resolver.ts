{% for model in cookiecutter.models.models_list %}import { inject, Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, ResolveFn, Router, RouterStateSnapshot } from '@angular/router';
import { catchError } from 'rxjs/operators';
import { {{ model.name }} } from '../models/domain/{{ model.name|lower }}';
import { {{ model.name }}Service } from '../services/api/{{ model.name|lower }}.service';
import { Observable, of } from 'rxjs';
import { GenericDetailResolver, GenericListResolver } from '../generics/generic-resolvers';

@Injectable({
    providedIn: 'root'
})
export class {{ model.name }}DetailResolver extends GenericDetailResolver<{{ model.name }}> {

    constructor(
        service: {{ model.name }}Service, 
        router: Router
    ) {
        super(service, router);
    }
}

@Injectable({
    providedIn: 'root'
})
export class {{ model.name }}ListResolver extends GenericListResolver<{{ model.name }}> {

    constructor(
        service: {{ model.name }}Service, 
        router: Router
    ) {
        super(service, router);
    }
}
--- split: src/app/shared/resolvers/{{ model.name|lower }}.resolver.ts
{% endfor %}
