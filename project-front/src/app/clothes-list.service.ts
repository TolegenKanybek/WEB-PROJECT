import { Injectable } from '@angular/core';
import { Clothes } from './clothes';
import {Observable} from 'rxjs';
import { HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ClothesListService {
  BASE_URL='http://localhost:8000';


  constructor(
    private http: HttpClient) { }

  getClothesList(): Observable<Clothes[]> {
    return this.http.get<Clothes[]>(`${this.BASE_URL}/core/clothes/`);
  }
  getClothesByCategory(id: number): Observable<Clothes[]> {
    return this.http.get<Clothes[]>(`${this.BASE_URL}/core/categories/${id}/clothes/`);
  }
  getCategoryName(id: number): Observable<any> {
    return this.http.get(`${this.BASE_URL}/core/categories/${id}`);
  }
  
}