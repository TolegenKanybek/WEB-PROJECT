import { Injectable } from '@angular/core';
import { Observable,of } from 'rxjs';
import {products} from './products';


@Injectable({
    providedIn:'root'
})

export class ProductService{
    constructor(){}

    getProduct(productId:number):Observable<any>{
        return of(products.find(product=>product.productId===productId));
    }

    getProducts():Observable<any>{
        return of(products);
    }

    getProductsByCategoryId(productId:number):Observable<any>{
        return of(products.filter(product=>product.categoryId===productId));
    }
}

