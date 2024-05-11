import { Injectable } from '@angular/core';
import { Cookie } from '../../models/domain/cookie';
import { HttpClient } from '@angular/common/http';
import { GenericApiService } from '../../generics/generic-api-service';

@Injectable({
  providedIn: 'root'
})
export class CookieService extends GenericApiService<Cookie> {

  constructor(http: HttpClient) { 
    super(http, '/api/cookie/');
  }
}
