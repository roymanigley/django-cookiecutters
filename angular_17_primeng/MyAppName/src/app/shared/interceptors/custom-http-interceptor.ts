import { Injectable } from '@angular/core';
import {
  HttpEvent,
  HttpInterceptor,
  HttpHandler,
  HttpRequest,
} from '@angular/common/http';
import { catchError, mergeMap, Observable, of, tap } from 'rxjs';
import { Router } from '@angular/router';
import { LoginService } from '../services/auth/login.service';


@Injectable({
  providedIn: 'root'
})
export class CustomHttpInterceptor implements HttpInterceptor {
  constructor(
    private router: Router,
    private loginService: LoginService
  ) {}

  intercept(
    request: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    return next.handle(request).pipe(
      catchError(err => {
        if (err.status == 401) {
          return this.loginService.refresh().pipe(
            mergeMap(() => next.handle(request)),
            catchError(() => {
              this.router.navigate(['/login']);
              throw err;
            })
          )
        } else {
          throw err;
        }
      })
    );
  }
}