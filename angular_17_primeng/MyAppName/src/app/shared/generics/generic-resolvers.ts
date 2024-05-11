import { ActivatedRouteSnapshot, Resolve, Router, RouterStateSnapshot } from '@angular/router';
import { catchError } from 'rxjs/operators';
import { Observable, of } from 'rxjs';
import { GenericApiService, IPage } from './generic-api-service';

export class GenericDetailResolver<T> implements Resolve<T|null> {

    constructor(
        private apiService: GenericApiService<T>, 
        private router: Router
    ) {}

    resolve(
        route: ActivatedRouteSnapshot, 
        state: RouterStateSnapshot
    ): Observable<T|null> {
        const id = route.params['id'];
        return this.apiService.getOne(id).pipe(
            catchError(error => {
                if (error.status === 404) {
                    this.router.navigate(['/404']);
                    return of(null);
                }
                throw error;
            })
        );
    }
}

export class GenericListResolver<T> implements Resolve<IPage<T>|null> {

    constructor(
        private apiService: GenericApiService<T>, 
        private router: Router
    ) {}

    resolve(
        route: ActivatedRouteSnapshot, 
        state: RouterStateSnapshot
    ): Observable<IPage<T>|null> {
        const cookieId = route.params['id'];
        return this.apiService.getList(route.queryParams).pipe(
            catchError(error => {
                if (error.status === 404) {
                    this.router.navigate(['/404']);
                    return of(null);
                }
                throw error;
            })
        );
    }
}