from django.urls import path
from api.views.views_fbv import *
from api.views.views_cbv import *


from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', CompanyListAPIView.as_view()),
    #path('companies/<int:company_id>/', company_details),
    path('companies/<int:company_id>/vacancies/', company_vacancies),
    #path('vacancies/', VacancyDetailAPIView.as_view()),
    #path('vacancies/<int:vacancy_id>', VacancyDetailAPIView.as_view()),
    #path('vacancies/top_ten', TopTenAPIView.as_view()),



]
