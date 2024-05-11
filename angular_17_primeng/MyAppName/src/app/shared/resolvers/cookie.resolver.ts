import { inject, Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, ResolveFn, Router, RouterStateSnapshot } from '@angular/router';
import { catchError } from 'rxjs/operators';
import { Cookie } from '../models/domain/cookie';
import { CookieService } from '../services/api/cookie.service';
import { Observable, of } from 'rxjs';
import { GenericDetailResolver, GenericListResolver } from '../generics/generic-resolvers';

@Injectable({
    providedIn: 'root'
})
export class CookieDetailResolver extends GenericDetailResolver<Cookie> {

    constructor(
        cookieService: CookieService, 
        router: Router
    ) {
        super(cookieService, router);
    }
}
@Injectable({
    providedIn: 'root'
})
export class CookieListResolver extends GenericListResolver<Cookie> {

    constructor(
        cookieService: CookieService, 
        router: Router
    ) {
        super(cookieService, router);
    }
}