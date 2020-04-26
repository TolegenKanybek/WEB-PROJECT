import { Injectable } from '@angular/core';
import { Category } from './category';
//import { CATEGORIES } from './categories-list';
import {Observable, of} from 'rxjs'
import { HttpClient } from '@angular/common/http';
import {LoginResponse} from './authetication';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {
  BASE_URL='http://127.0.0.1:8000';

  //categories = CATEGORIES

  constructor(private http:HttpClient) { }

  getCategories(): Observable<Category[]> {
    return this.http.get<Category[]>(`${this.BASE_URL}/core/categories/`);
  }
  


  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/core/login/`, {
      username,
      password
    });
  }
}