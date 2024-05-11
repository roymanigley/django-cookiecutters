import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, of, tap } from 'rxjs';
import { IUser } from '../../models/auth/user';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private currentUser?: IUser;

  constructor(
    private http: HttpClient
  ) { }

  login(payload: any): Observable<IUser> {
    return this.http.post('/auth/login/', payload).pipe(
      tap((response: any) => this.currentUser = response.user)
    )
  }

  logout(): Observable<void> {
    this.currentUser = undefined;
    return this.http.post<void>('/auth/logout/', null);
  }

  getCurrentUser(): Observable<IUser> {
    if (this.currentUser) {
      return of(this.currentUser);
    } else {
      return this.http.get('/auth/user/').pipe(
        tap((user: any) => this.currentUser = user)
      );
    }
  }

  refresh(): Observable<void> {
    return this.http.post<void>('/auth/token/refresh/', null).pipe(
      catchError(err => {
        this.currentUser = undefined;
        throw err;
      })
    );
  }
}