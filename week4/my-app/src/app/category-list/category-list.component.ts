import { Component, OnInit } from '@angular/core';
import { categories } from '../categories';
import {ProductService} from '../product.service';
import {CategoryService} from '../category.service';
import {ActivatedRoute,Router} from '@angular/router';



@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrls: ['./category-list.component.css']
})
export class CategoryListComponent implements OnInit {
  products:any;
  category:any;
  categories=categories
  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private productService: ProductService,
    private categoryService: CategoryService
  ) {
    this.router.events.subscribe((value => {
      this.getProducts();
      this.getCategory();
    }));
   }

  ngOnInit(): void {
    this.getProducts();
    this.getCategory();
  }

  getProducts() {
    const id = +this.route.snapshot.paramMap.get('productId');
    this.productService.getProductsByCategoryId(id).subscribe(products => this.products = products);
  }

  getCategory() {
    const id = +this.route.snapshot.paramMap.get('categoryId');
    this.categoryService.getCategory(id).subscribe(category => this.category = category);
  }

}
