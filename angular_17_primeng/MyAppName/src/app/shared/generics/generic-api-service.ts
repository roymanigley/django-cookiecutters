import { HttpClient, HttpParams } from "@angular/common/http";
import { filter, map, Observable } from "rxjs";
import { DEFAULT_PAGE_SIZE } from "../constants";

export interface IPage<T> {
    page: number,
    size: number,
    count: number,
    results: T[]
}

export class GenericApiService<T> {

    constructor(
        protected http: HttpClient,
        protected baseUrl: string
    ) {}

    getList(params: any = {}): Observable<IPage<T>> {
        const _params = {
            page: 1, size: DEFAULT_PAGE_SIZE, filter: null
        }
        Object.assign(_params, params);
        const httpParams = this.toHttpParams(_params);
        return this.http.get<IPage<T>>(this.baseUrl, {params: httpParams, observe: 'response'}).pipe(
            map(response => {
                return {
                    page: _params.page as number,
                    size: _params.size as number,
                    count: parseInt(response.headers.get('X-Total-Count') ?? '-1', 10),
                    results: response.body ?? []
                } as IPage<T>;
            })
        );
    }
    getOne(id: number, params: any = {}): Observable<T> {
        const httpParams = this.toHttpParams(params);
        return this.http.get<T>(this.baseUrl + id + '/', {params: httpParams});
    }
    delete(id: number, params: any = {}): Observable<T> {
        const httpParams = this.toHttpParams(params);
        return this.http.delete<T>(this.baseUrl + id + '/', {params: httpParams});
    }
    create(record: T, params: any = {}): Observable<T> {
        const httpParams = this.toHttpParams(params);
        return this.http.post<T>(this.baseUrl, record, {params: httpParams});
    }
    update(id: number, record: T, params: any = {}): Observable<T> {
        const httpParams = this.toHttpParams(params);
        return this.http.put<T>(this.baseUrl + id + '/', record, {params: httpParams});
    }

    protected toHttpParams(params: any = {}): HttpParams {
        let httpParams = new HttpParams()
        Object.keys(params).forEach(key => {
            if (params[key]) {
                httpParams = httpParams.append(key, params[key])
            }
        });
        return httpParams;
    }
}