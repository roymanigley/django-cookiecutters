import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LocalStorageService {

  constructor() { }

  get(key: LocalStorageKey): any {
    localStorage.getItem(key)
  }

  set(key: LocalStorageKey, value: any) {
    localStorage.setItem(key, value)
  }
}

export enum LocalStorageKey {
  LANGUAGE = 'LANGUAGE'
}