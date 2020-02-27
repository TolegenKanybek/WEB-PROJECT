import {Injectable} from '@angular/core';
import {Observable,of} from 'rxjs'; 
import {categories} from './categories';

@Injectable({
    providedIn:'root'
})

export class CategoryService{
    constructor(){}

    getCategory(categoryId: number): Observable<any> {
    return of(categories.find(category => category.categoryId === categoryId));
  }

  getCategories(): Observable<any> {
    return of(categories);
  }
}