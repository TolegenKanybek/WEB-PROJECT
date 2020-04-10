from django.urls import path

from api.views import company_list, company_details, top_ten
from api.views import company_vacancies, vacancies_list, vacancy_detail

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_details),
    path('companies/<int:company_id>/vacancies/', company_vacancies),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>', vacancy_detail),
    path('vacancies/top_ten', top_ten),
]
